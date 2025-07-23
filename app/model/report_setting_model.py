from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.util.database import Base

class ReportSetting(Base):
    __tablename__ = 'report_setting'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project_info.id'), nullable=False, comment='所属项目')
    setting_name = Column(String(128), nullable=False, comment='设定项名称')
    value = Column(String(256), nullable=False, comment='设定值')
    remark = Column(Text, comment='备注') 