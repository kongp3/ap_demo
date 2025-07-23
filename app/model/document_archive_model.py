from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.util.database import Base

class DocumentArchive(Base):
    __tablename__ = 'document_archive'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project_info.id'), nullable=False, comment='所属项目')
    file_name = Column(String(256), nullable=False, comment='文件名')
    file_path = Column(String(512), nullable=False, comment='文件路径')
    remark = Column(Text, comment='备注') 