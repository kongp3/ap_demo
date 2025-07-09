from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.util.database import Base

class AuditDraft(Base):
    __tablename__ = 'audit_draft'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')
    company_name = Column(String(128), nullable=False, comment='公司名称')
    status = Column(String(16), nullable=False, comment='底稿状态')
    matter = Column(String(64), nullable=False, comment='审计事项')
    name = Column(String(1000), nullable=False, comment='底稿名称')
    code = Column(String(16), nullable=False, comment='底稿编码')
    focus = Column(String(128), comment='关联关注点')
    operator = Column(String(64), nullable=False, comment='取证人')
    draft_id = Column(Integer, ForeignKey('audit_draft.id'), comment='引用底稿ID')
    source = Column(String(256), nullable=False, comment='记录来源')
    model = Column(String(16), nullable=False, comment='风险模版')
    create_time = Column(DateTime, nullable=False, comment='创建时间')
    update_time = Column(DateTime, nullable=False, comment='变更时间')

    # 自引用关系
    referenced_draft = relationship(
        "AuditDraft",
        remote_side=[id],
        backref="referencing_drafts",
        foreign_keys=[draft_id]
    )