from sqlalchemy import Column, Integer, String, Text
from app.util.database import Base

class ProjectInfo(Base):
    __tablename__ = 'project_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False, comment='项目名称')
    audit_unit = Column(String(128), nullable=False, comment='审计单位')
    type = Column(String(64), nullable=False, comment='项目类型')
    leader = Column(String(64), nullable=False, comment='项目负责人')
    remark = Column(Text, comment='备注') 