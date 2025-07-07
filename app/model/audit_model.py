from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.util.database import Base

class AuditResult(Base):
    __tablename__ = 'audit_result'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(Text, comment='企业名称')
    process = Column(Text, comment='审计过程')
    conclusion = Column(Text, comment='审计结论')

    details = relationship("AuditResultDetail", back_populates="audit")


class AuditResultDetail(Base):
    __tablename__ = 'audit_result_detail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    audit_id = Column(Integer, ForeignKey('audit_result.id'))
    customer_name = Column(String(256), nullable=False)
    title = Column(String(500))
    level = Column(String(16))
    desc = Column(Text, comment='问题描述')
    suggest = Column(Text, comment='审计建议')
    date_time = Column(DateTime)

    audit = relationship("AuditResult", back_populates="details")
    attachments = relationship("AuditResultAttach", back_populates="detail")


class AuditResultAttach(Base):
    __tablename__ = 'audit_result_attach'

    id = Column(Integer, primary_key=True, autoincrement=True)
    detail_id = Column(Integer, ForeignKey('audit_result_detail.id'))
    name = Column(String(1000))
    url = Column(String(2000))
    filesize = Column(Integer)
    date_time = Column(DateTime)

    detail = relationship("AuditResultDetail", back_populates="attachments")