# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# import when
# from schemer import Schema, Array
from repository.mysql.audit_pioneer import CompanyRepository
from repository.mysql import get_session

# from repository.common.common_repository import CommonRepository


'''
“问题编号”-q_no，
“问题标题”-q_title，
“问题点”-q_point，
“涉及金额(万元)”-amount，
“涉及数量(个)”-q_num，
“问题发现人”-q_finder
'''


def get_result():
    print('获取AI得出的结果')
    session = get_session()
    try:
        cr = CompanyRepository(session)
        results = cr.find_all()
        return results

    except Exception():
        raise Exception("Mysql excute failed...")
    finally:
        session.close()

