from app.model.report_setting_model import ReportSetting
from app.model.project_info_model import ProjectInfo
from app.util.database import db_session
from sqlalchemy.exc import SQLAlchemyError

class ReportSettingService:
    @staticmethod
    def list():
        """
        查询所有入报设定信息
        :return: 设定列表或错误信息
        """
        try:
            settings = db_session.query(ReportSetting).all()
            return [ReportSettingService.to_dict(s) for s in settings]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def get_by_id(item_id):
        """
        按主键查询入报设定信息
        :param item_id: 设定ID
        :return: 设定信息或错误信息
        """
        try:
            setting = db_session.query(ReportSetting).filter_by(id=item_id).first()
            if not setting:
                return None
            return ReportSettingService.to_dict(setting)
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def query_by_attr(**kwargs):
        """
        按指定属性查询入报设定信息，返回列表
        :param kwargs: 属性名=属性值
        :return: 设定列表或错误信息
        """
        try:
            settings = db_session.query(ReportSetting).filter_by(**kwargs).all()
            return [ReportSettingService.to_dict(s) for s in settings]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def paginate(page=1, per_page=10, **kwargs):
        """
        分页查询入报设定信息，可带属性过滤
        :param page: 页码
        :param per_page: 每页数量
        :param kwargs: 属性名=属性值
        :return: 分页结果dict
        """
        try:
            query = db_session.query(ReportSetting)
            if kwargs:
                query = query.filter_by(**kwargs)
            total = query.count()
            items = query.offset((page-1)*per_page).limit(per_page).all()
            return {
                'total': total,
                'page': page,
                'per_page': per_page,
                'items': [ReportSettingService.to_dict(s) for s in items]
            }
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def add(item):
        """
        新增入报设定，包含外键和唯一性校验
        :param item: dict
        :return: 结果dict
        """
        required = ['project_id', 'setting_name', 'value']
        for f in required:
            if not item.get(f):
                return {'msg': f'{f}为必填项', 'error': True}
        # 外键存在性校验
        project = db_session.query(ProjectInfo).filter_by(id=item['project_id']).first()
        if not project:
            return {'msg': '所属项目不存在', 'error': True}
        # 同项目设定项名称唯一
        exists = db_session.query(ReportSetting).filter_by(project_id=item['project_id'], setting_name=item['setting_name']).first()
        if exists:
            return {'msg': '同项目下设定项名称已存在', 'error': True}
        try:
            setting = ReportSetting(
                project_id=item['project_id'],
                setting_name=item['setting_name'],
                value=item['value'],
                remark=item.get('remark')
            )
            db_session.add(setting)
            db_session.commit()
            return {'msg': '添加成功', 'item': ReportSettingService.to_dict(setting)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def update(item_id, item):
        """
        更新入报设定，包含外键和唯一性校验
        :param item_id: 设定ID
        :param item: dict
        :return: 结果dict
        """
        try:
            setting = db_session.query(ReportSetting).filter_by(id=item_id).first()
            if not setting:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            # 外键存在性校验
            if 'project_id' in item and item['project_id'] != setting.project_id:
                project = db_session.query(ProjectInfo).filter_by(id=item['project_id']).first()
                if not project:
                    return {'msg': '所属项目不存在', 'error': True}
            # 同项目设定项名称唯一
            if 'setting_name' in item and (item['setting_name'] != setting.setting_name or ('project_id' in item and item['project_id'] != setting.project_id)):
                pid = item.get('project_id', setting.project_id)
                exists = db_session.query(ReportSetting).filter_by(project_id=pid, setting_name=item['setting_name']).first()
                if exists:
                    return {'msg': '同项目下设定项名称已存在', 'error': True}
            for f in ['project_id', 'setting_name', 'value']:
                if f in item and not item[f]:
                    return {'msg': f'{f}为必填项', 'error': True}
            for k, v in item.items():
                setattr(setting, k, v)
            db_session.commit()
            return {'msg': '更新成功', 'item': ReportSettingService.to_dict(setting)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def delete(item_id):
        """
        删除入报设定
        :param item_id: 设定ID
        :return: 结果dict
        """
        try:
            setting = db_session.query(ReportSetting).filter_by(id=item_id).first()
            if not setting:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            db_session.delete(setting)
            db_session.commit()
            return {'msg': '删除成功', 'item_id': item_id}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def to_dict(obj):
        """
        ORM对象转dict
        :param obj: ReportSetting对象
        :return: dict
        """
        return {
            'id': obj.id,
            'project_id': obj.project_id,
            'setting_name': obj.setting_name,
            'value': obj.value,
            'remark': obj.remark
        } 