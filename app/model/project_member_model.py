from sqlalchemy import Column, Integer, String, ForeignKey
from app.util.database import Base

class ProjectMember(Base):
    __tablename__ = 'project_member'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project_info.id'), nullable=False, comment='所属项目')
    username = Column(String(64), nullable=False, comment='成员姓名')
    role = Column(String(32), nullable=False, comment='角色')
    organization = Column(String(128), comment='所属机构')
    audit_unit = Column(String(128), comment='审计单位') 