from datetime import datetime
from sqlalchemy.orm import Session
from app.model.draft_model import AuditDraft
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import delete, desc
from app.model import draft_model


def save_audit_draft(db: Session, draft_data: dict):
    """
    保存审计底稿
    """
    try:
        # 删除被审计单位底稿
        delete_drafts_by_company(db, company_name=draft_data["company_name"])

        # 创建审计底稿记录
        draft = AuditDraft(
            company_name=draft_data["company_name"],
            status=draft_data["status"],
            matter=draft_data["matter"],
            name=draft_data["name"],
            code=draft_data["code"],
            focus=draft_data["focus"],
            operator=draft_data["operator"],
            source=draft_data["source"],
            model=draft_data["model"],
            draft_id=draft_data.get("draft_id"),
            create_time=datetime.now(),
            update_time=datetime.now()
        )

        db.add(draft)
        db.commit()
        db.refresh(draft)

        return draft
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_first_draft(db: Session):
    """
    根据公司名称查询审计底稿
    """
    try:
        # 按创建时间降序排序，获取最新的第一条记录
        draft = db.query(AuditDraft).order_by(desc(AuditDraft.create_time)).first()
        return draft
    except SQLAlchemyError as e:
        raise e


def get_draft_details(db: Session, draft_id: int):
    """
    获取底稿详细信息（包括引用的底稿）
    """
    try:
        # 获取主底稿
        main_draft = db.query(AuditDraft).filter(
            AuditDraft.id == draft_id
        ).first()

        if not main_draft:
            return None

        # 获取引用的底稿（如果有）
        referenced_drafts = []
        if main_draft.draft_id:
            referenced = db.query(AuditDraft).filter(
                AuditDraft.id == main_draft.draft_id
            ).first()
            if referenced:
                referenced_drafts.append(referenced)

        # 获取引用当前底稿的其他底稿
        referencing_drafts = db.query(AuditDraft).filter(
            AuditDraft.draft_id == draft_id
        ).all()

        return {
            "main_draft": main_draft,
            "referenced_drafts": referenced_drafts,
            "referencing_drafts": referencing_drafts
        }
    except SQLAlchemyError as e:
        raise e

def delete_drafts_by_company(db: Session, company_name: str):
    """
    根据公司名称删除审计底稿
    """
    try:
        # 第一步：查询所有相关底稿ID
        draft_ids = db.query(draft_model.AuditDraft.id).filter(
            draft_model.AuditDraft.company_name.ilike(f"%{company_name}%")
        ).all()
        draft_ids = [id[0] for id in draft_ids]

        if not draft_ids:
            return 0, 0

        # 第二步：解除其他底稿对这些底稿的引用
        if draft_ids:
            stmt = delete(draft_model.AuditDraft).where(
                draft_model.AuditDraft.id.in_(draft_ids)
            )
            result = db.execute(stmt)
            references_cleared = result.rowcount

        # 第三步：删除底稿
        stmt = delete(draft_model.AuditDraft).where(
            draft_model.AuditDraft.id.in_(draft_ids)
        )
        result = db.execute(stmt)
        drafts_deleted = result.rowcount

        db.commit()

        return drafts_deleted, references_cleared

    except Exception as e:
        db.rollback()
        raise e