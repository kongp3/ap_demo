import random
from datetime import datetime
from app.model.audit_model import AuditResult, AuditResultDetail, AuditResultAttach
from sqlalchemy.orm import Session
from sqlalchemy import delete, desc
from app.model import audit_model

def save_audit_data(db: Session, audit_data: dict):
    # 删除被审计单位结果
    delete_audit_results_by_company(db, company_name=audit_data["company_name"])

    # 创建主审计记录
    audit = AuditResult(
        company_name=audit_data['company_name'],
        process=audit_data["process"],
        conclusion=audit_data["conclusion"]
    )
    db.add(audit)
    db.flush()  # 获取生成的ID但不提交事务

    # 创建客商详情记录
    for customer in audit_data["customers"]:
        detail = AuditResultDetail(
            audit_id=audit.id,
            customer_name=customer["customer_name"],
            title=customer["title"],
            level=customer["level"],
            desc=customer["desc"],
            suggest=customer["suggest"],
            date_time=datetime.now()
        )
        db.add(detail)
        db.flush()  # 获取生成的ID但不提交事务

        attach = AuditResultAttach(
            detail_id=detail.id,
            name= "对" +detail.customer_name + "的审计建议",
            url=customer["attach_url"],
            filesize= 1024,
            date_time=datetime.now()
        )
        db.add(attach)

    db.commit()
    return audit.id

def get_audit(db: Session):
    """
    根据客商名称查询审计结果
    :param db: 数据库会话
    :return: 审计结果字典
    """
    # 按创建时间降序排序，获取最新的第一条记录
    audit = db.query(AuditResult).first()

    if not audit:
        return None

    # 获取该审计的所有客商详情
    details = db.query(AuditResultDetail).filter(
        AuditResultDetail.audit_id.ilike(audit.id)
    ).all()

    # 构建客商信息列表
    customers = []
    for detail in details:
        customers.append({
            "detail_id": detail.id,
            "customer_name": detail.customer_name,
            "title": detail.title,
            "level": detail.level
        })

    return {
        "audit_id": audit.id,
        "process": audit.process,
        "conclusion": audit.conclusion,
        "customer": customers
    }

def get_audit_by_company_name(db: Session, company_name: str):
    """
    根据客商名称查询审计结果
    :param db: 数据库会话
    :param company_name: 企业名称
    :return: 审计结果字典
    """
    # 查询包含指定客商名称的审计详情
    companies = db.query(AuditResult).filter(
        AuditResult.company_name.ilike(f"%{company_name}%")
    ).all()

    if not companies:
        return None

    # 构建响应数据
    results = []
    for audit in companies:

        # 获取该审计的所有客商详情
        details = db.query(AuditResultDetail).filter(
            AuditResultDetail.audit_id.ilike(audit.id)
        ).all()

        # 构建客商信息列表
        customers = []
        for detail in details:
            customers.append({
                "customer_name": detail.customer_name,
                "title": detail.title,
                "level": detail.level
            })

        results.append({
            "audit_id": audit.id,
            "process": audit.process,
            "conclusion": audit.conclusion,
            "customer": customers
        })

    return results


def get_customer_detail_by_audit_id(db: Session, audit_id: int):
    """
    根据审计ID查询客商详情
    :param db: 数据库会话
    :param audit_id: 审计ID
    :return: 客商详情字典
    """
    # 查询该审计的所有客商详情
    details = db.query(AuditResultDetail).filter(
        AuditResultDetail.audit_id == audit_id
    ).all()

    # 构建响应数据
    results = []
    for detail in details:
        # 查询附件
        attachments = db.query(AuditResultAttach).filter(
            AuditResultAttach.detail_id == detail.id
        ).all()

        # 构建附件列表
        attach_list = []
        for attach in attachments:
            attach_list.append({
                "name": attach.name,
                "url": attach.url,
                "filesize": attach.filesize,
                "dateTime": attach.date_time.isoformat() if attach.date_time else None
            })

        # 添加客商详情
        results.append({
            "customer_name": detail.customer_name,
            "title": detail.title,
            "level": detail.level,
            "desc": detail.desc,
            "suggest": detail.suggest,
            "attach": attach_list
        })

    return results

def get_customer_detail(db: Session, detail_id: int):
    """
    根据审计ID查询客商详情
    :param db: 数据库会话
    :param audit_id: 审计ID
    :return: 客商详情字典
    """
    # 查询该审计的所有客商详情
    detail = db.query(AuditResultDetail).filter(
        AuditResultDetail.id == detail_id
    ).one()

    if not detail:
        return None

    # 查询附件
    attachments = db.query(AuditResultAttach).filter(
        AuditResultAttach.detail_id == detail.id
    ).all()

    # 构建附件列表
    attach_list = []
    for attach in attachments:
        attach_list.append({
            "name": attach.name,
            "url": attach.url,
            "filesize": attach.filesize,
            "dateTime": attach.date_time.strftime("%Y-%m-%d %H:%M:%S") if attach.date_time else None
        })

    return {
        "customer_name": detail.customer_name,
        "title": detail.title,
        "level": detail.level,
        "desc": detail.desc,
        "suggest": detail.suggest,
        "attach": attach_list
    }


def delete_audit_results_by_company(db: Session, company_name: str):
    """
    根据公司名称删除审计结果及相关数据
    """
    try:
        # 第一步：查询相关审计结果ID
        audit_ids = db.query(audit_model.AuditResult.id).filter(
            audit_model.AuditResult.company_name.ilike(f"%{company_name}%")
        ).distinct().all()
        audit_ids = [id[0] for id in audit_ids]

        # 第四步：删除审计主结果
        stmt = delete(audit_model.AuditResult).where(
            audit_model.AuditResult.id.in_(audit_ids)
        )
        result = db.execute(stmt)
        audit_deleted = result.rowcount

        if not audit_ids:
            return 0, 0, 0

        # 第二步：删除相关附件
        # 先查询相关detail_id
        detail_ids = db.query(audit_model.AuditResultDetail.id).filter(
            audit_model.AuditResultDetail.audit_id.in_(audit_ids)
        ).all()
        detail_ids = [id[0] for id in detail_ids]

        attach_deleted = 0
        if detail_ids:
            stmt = delete(audit_model.AuditResultAttach).where(
                audit_model.AuditResultAttach.detail_id.in_(detail_ids)
            )
            result = db.execute(stmt)
            attach_deleted = result.rowcount

        # 第三步：删除审计详情
        stmt = delete(audit_model.AuditResultDetail).where(
            audit_model.AuditResultDetail.audit_id.in_(audit_ids)
        )
        result = db.execute(stmt)
        detail_deleted = result.rowcount

        db.commit()

        return audit_deleted, detail_deleted, attach_deleted

    except Exception as e:
        db.rollback()
        raise e