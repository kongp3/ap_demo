from app.model.project_info_model import ProjectInfo
from app.model.project_member_model import ProjectMember
from app.model.audit_plan_model import AuditPlan
from app.model.document_archive_model import DocumentArchive
from app.model.report_setting_model import ReportSetting
from app.util.database import db_session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound

class ProjectInfoService:
    @staticmethod
    def list():
        """
        查询所有项目信息
        :return: 项目列表或错误信息
        """
        try:
            projects = db_session.query(ProjectInfo).all()
            return [ProjectInfoService.to_dict(p) for p in projects]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def get_by_id(item_id):
        """
        按主键查询项目信息
        :param item_id: 项目ID
        :return: 项目信息或错误信息
        """
        try:
            project = db_session.query(ProjectInfo).filter_by(id=item_id).first()
            if not project:
                return None
            return ProjectInfoService.to_dict(project)
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def query_by_attr(**kwargs):
        """
        按指定属性查询项目信息，返回列表
        :param kwargs: 属性名=属性值
        :return: 项目列表或错误信息
        """
        try:
            projects = db_session.query(ProjectInfo).filter_by(**kwargs).all()
            return [ProjectInfoService.to_dict(p) for p in projects]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def paginate(page=1, per_page=10, **kwargs):
        """
        分页查询项目信息，可带属性过滤
        :param page: 页码
        :param per_page: 每页数量
        :param kwargs: 属性名=属性值
        :return: 分页结果dict
        """
        try:
            query = db_session.query(ProjectInfo)
            if kwargs:
                query = query.filter_by(**kwargs)
            total = query.count()
            items = query.offset((page-1)*per_page).limit(per_page).all()
            return {
                'total': total,
                'page': page,
                'per_page': per_page,
                'items': [ProjectInfoService.to_dict(p) for p in items]
            }
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def add(item):
        """
        新增项目信息，包含唯一性校验
        :param item: dict
        :return: 结果dict
        """
        required = ['name', 'audit_unit', 'type', 'leader']
        for f in required:
            if not item.get(f):
                return {'msg': f'{f}为必填项', 'error': True}
        # 唯一性校验
        exists = db_session.query(ProjectInfo).filter_by(name=item['name']).first()
        if exists:
            return {'msg': '项目名称已存在', 'error': True}
        try:
            project = ProjectInfo(
                name=item['name'],
                audit_unit=item['audit_unit'],
                type=item['type'],
                leader=item['leader'],
                remark=item.get('remark')
            )
            db_session.add(project)
            db_session.commit()
            return {'msg': '添加成功', 'item': ProjectInfoService.to_dict(project)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def update(item_id, item):
        """
        更新项目信息，包含唯一性校验
        :param item_id: 项目ID
        :param item: dict
        :return: 结果dict
        """
        try:
            project = db_session.query(ProjectInfo).filter_by(id=item_id).first()
            if not project:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            # 名称唯一性校验
            if 'name' in item and item['name'] != project.name:
                exists = db_session.query(ProjectInfo).filter_by(name=item['name']).first()
                if exists:
                    return {'msg': '项目名称已存在', 'error': True}
            for f in ['name', 'audit_unit', 'type', 'leader']:
                if f in item and not item[f]:
                    return {'msg': f'{f}为必填项', 'error': True}
            for k, v in item.items():
                setattr(project, k, v)
            db_session.commit()
            return {'msg': '更新成功', 'item': ProjectInfoService.to_dict(project)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def delete(item_id):
        """
        删除项目信息，依赖性校验
        :param item_id: 项目ID
        :return: 结果dict
        """
        try:
            project = db_session.query(ProjectInfo).filter_by(id=item_id).first()
            if not project:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            # 依赖性校验
            if db_session.query(ProjectMember).filter_by(project_id=item_id).first():
                return {'msg': '存在项目成员，无法删除', 'error': True}
            if db_session.query(AuditPlan).filter_by(project_id=item_id).first():
                return {'msg': '存在审计方案，无法删除', 'error': True}
            if db_session.query(DocumentArchive).filter_by(project_id=item_id).first():
                return {'msg': '存在文书归档，无法删除', 'error': True}
            if db_session.query(ReportSetting).filter_by(project_id=item_id).first():
                return {'msg': '存在入报设定，无法删除', 'error': True}
            db_session.delete(project)
            db_session.commit()
            return {'msg': '删除成功', 'item_id': item_id}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def to_dict(obj):
        """
        ORM对象转dict
        :param obj: ProjectInfo对象
        :return: dict
        """
        return {
            'id': obj.id,
            'name': obj.name,
            'audit_unit': obj.audit_unit,
            'type': obj.type,
            'leader': obj.leader,
            'remark': obj.remark
        } 