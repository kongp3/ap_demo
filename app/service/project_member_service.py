from app.model.project_member_model import ProjectMember
from app.model.project_info_model import ProjectInfo
from app.util.database import db_session
from sqlalchemy.exc import SQLAlchemyError

class ProjectMemberService:
    @staticmethod
    def list():
        """
        查询所有项目成员信息
        :return: 成员列表或错误信息
        """
        try:
            members = db_session.query(ProjectMember).all()
            return [ProjectMemberService.to_dict(m) for m in members]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def get_by_id(item_id):
        """
        按主键查询项目成员信息
        :param item_id: 成员ID
        :return: 成员信息或错误信息
        """
        try:
            member = db_session.query(ProjectMember).filter_by(id=item_id).first()
            if not member:
                return None
            return ProjectMemberService.to_dict(member)
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def query_by_attr(**kwargs):
        """
        按指定属性查询项目成员信息，返回列表
        :param kwargs: 属性名=属性值
        :return: 成员列表或错误信息
        """
        try:
            members = db_session.query(ProjectMember).filter_by(**kwargs).all()
            return [ProjectMemberService.to_dict(m) for m in members]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def paginate(page=1, per_page=10, **kwargs):
        """
        分页查询项目成员信息，可带属性过滤
        :param page: 页码
        :param per_page: 每页数量
        :param kwargs: 属性名=属性值
        :return: 分页结果dict
        """
        try:
            query = db_session.query(ProjectMember)
            if kwargs:
                query = query.filter_by(**kwargs)
            total = query.count()
            items = query.offset((page-1)*per_page).limit(per_page).all()
            return {
                'total': total,
                'page': page,
                'per_page': per_page,
                'items': [ProjectMemberService.to_dict(m) for m in items]
            }
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def add(item):
        """
        新增项目成员，包含外键和唯一性校验
        :param item: dict
        :return: 结果dict
        """
        required = ['project_id', 'username', 'role']
        for f in required:
            if not item.get(f):
                return {'msg': f'{f}为必填项', 'error': True}
        # 外键存在性校验
        project = db_session.query(ProjectInfo).filter_by(id=item['project_id']).first()
        if not project:
            return {'msg': '所属项目不存在', 'error': True}
        # 同项目成员姓名唯一
        exists = db_session.query(ProjectMember).filter_by(project_id=item['project_id'], username=item['username']).first()
        if exists:
            return {'msg': '同项目下成员姓名已存在', 'error': True}
        try:
            member = ProjectMember(
                project_id=item['project_id'],
                username=item['username'],
                role=item['role'],
                organization=item.get('organization'),
                audit_unit=item.get('audit_unit')
            )
            db_session.add(member)
            db_session.commit()
            return {'msg': '添加成功', 'item': ProjectMemberService.to_dict(member)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def update(item_id, item):
        """
        更新项目成员，包含外键和唯一性校验
        :param item_id: 成员ID
        :param item: dict
        :return: 结果dict
        """
        try:
            member = db_session.query(ProjectMember).filter_by(id=item_id).first()
            if not member:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            # 外键存在性校验
            if 'project_id' in item and item['project_id'] != member.project_id:
                project = db_session.query(ProjectInfo).filter_by(id=item['project_id']).first()
                if not project:
                    return {'msg': '所属项目不存在', 'error': True}
            # 同项目成员姓名唯一
            if 'username' in item and (item['username'] != member.username or ('project_id' in item and item['project_id'] != member.project_id)):
                pid = item.get('project_id', member.project_id)
                exists = db_session.query(ProjectMember).filter_by(project_id=pid, username=item['username']).first()
                if exists:
                    return {'msg': '同项目下成员姓名已存在', 'error': True}
            for f in ['project_id', 'username', 'role']:
                if f in item and not item[f]:
                    return {'msg': f'{f}为必填项', 'error': True}
            for k, v in item.items():
                setattr(member, k, v)
            db_session.commit()
            return {'msg': '更新成功', 'item': ProjectMemberService.to_dict(member)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def delete(item_id):
        """
        删除项目成员
        :param item_id: 成员ID
        :return: 结果dict
        """
        try:
            member = db_session.query(ProjectMember).filter_by(id=item_id).first()
            if not member:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            db_session.delete(member)
            db_session.commit()
            return {'msg': '删除成功', 'item_id': item_id}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def to_dict(obj):
        """
        ORM对象转dict
        :param obj: ProjectMember对象
        :return: dict
        """
        return {
            'id': obj.id,
            'project_id': obj.project_id,
            'username': obj.username,
            'role': obj.role,
            'organization': obj.organization,
            'audit_unit': obj.audit_unit
        } 