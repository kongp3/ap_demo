# -*- coding: utf-8 -*-

from repository.mysql import get_session, AuditResultAttachModel


class CompanyRepository(object):
    """ Account 存储类, 进出的一定都是account对象 """

    def __init__(self, session=None):
        self.session = session or get_session()

        # 决定是否自己销毁session, 而不是依赖上层回收
        if session is None:
            self.auto_close_session = True
        else:
            self.auto_close_session = False

    def __del__(self):
        try:
            if self.auto_close_session:
                self.session.close()
        except:
            pass


    def find_all(self):
        result_models = self.session.query(AuditResultAttachModel).all()
        results = []
        result_row = {}

        for result_model in result_models:

            result_row["q_no"] = "Q0000"+ str(result_model.id)  # “问题编号”
            result_row["q_title"] = str(result_model.audit_result_detail_model.title)  # “问题标题”
            result_row["q_point"] = str(result_model.audit_result_detail_model.desc)  # “问题点”-
            result_row["amount"] = ''  # “涉及金额(万元)”-
            result_row["q_num"] = ''  # “涉及数量(个)”-
            result_row["q_finder"] = 'AI助手'  # “问题发现人”-
            result_row["q_attach"] = result_model.url
            results.append(result_row)

        return results




