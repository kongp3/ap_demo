import random
from datetime import datetime
from app.model.audit_model import AuditResult, AuditResultDetail, AuditResultAttach
from sqlalchemy.orm import Session


def save_audit_data(db: Session, audit_data: dict):
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