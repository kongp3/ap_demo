# -*- coding: utf-8 -*-

import sys

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from config import MYSQL_CONN

import pymysql
pymysql.install_as_MySQLdb()

# reload(sys)
# sys.setdefaultencoding('utf8')

Base = automap_base()

# 数据库连接配置
database = create_engine(MYSQL_CONN, pool_recycle=120)


# 默认自动flush（一旦flush就能在query中拿到数据），但是不自动提交（不提交就不会真的写到数据库中去），
# 由程序自己控制，这样有利于事务的控制
DBSession = sessionmaker(bind=database, autoflush=True, autocommit=False, expire_on_commit=True)


def get_session():
    """ 每次返回一个session的实例就实际上从连接池里面拿走一个conn，从conn可以拿出一个transaction（事务）来用 """
    return DBSession()


class AuditResultModel(Base):
    __tablename__ = 'audit_result'

    id = Column(String, primary_key=True)
    # bank_account_models = relationship("BankAccountModel", backref="accounts")
    # transfer_models = relationship("TransferModel", backref="accounts")


class AuditResultDetailModel(Base):
    __tablename__ = 'audit_result_detail'
    id = Column(String, primary_key=True)
    audit_id = Column(String, ForeignKey('audit_result.id'))
    audit_result_model = relationship("AuditResultModel", backref="audit_result")


class AuditResultAttachModel(Base):
    __tablename__ = 'audit_result_attach'

    id = Column(String, primary_key=True)

    detail_id = Column(String, ForeignKey('audit_result_detail.id'))
    audit_result_detail_model = relationship("AuditResultDetailModel", backref="audit_result_detail")

Base.prepare(database, reflect=True)
