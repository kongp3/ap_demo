from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.util.database import Base

class AuditPlan(Base):
    __tablename__ = 'audit_plan'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project_info.id'), nullable=False, comment='所属项目')
    plan_name = Column(String(128), nullable=False, comment='方案名称')
    items = Column(Text, nullable=False, comment='审计事项（JSON字符串）')
    remark = Column(Text, comment='备注') 