from app.model.audit_plan_model import AuditPlan
from app.model.project_info_model import ProjectInfo
from app.util.database import db_session
from sqlalchemy.exc import SQLAlchemyError

class AuditPlanService:
    @staticmethod
    def list():
        """
        查询所有审计方案信息
        :return: 方案列表或错误信息
        """
        try:
            plans = db_session.query(AuditPlan).all()
            return [AuditPlanService.to_dict(p) for p in plans]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def get_by_id(item_id):
        """
        按主键查询审计方案信息
        :param item_id: 方案ID
        :return: 方案信息或错误信息
        """
        try:
            plan = db_session.query(AuditPlan).filter_by(id=item_id).first()
            if not plan:
                return None
            return AuditPlanService.to_dict(plan)
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def query_by_attr(**kwargs):
        """
        按指定属性查询审计方案信息，返回列表
        :param kwargs: 属性名=属性值
        :return: 方案列表或错误信息
        """
        try:
            plans = db_session.query(AuditPlan).filter_by(**kwargs).all()
            return [AuditPlanService.to_dict(p) for p in plans]
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def paginate(page=1, per_page=10, **kwargs):
        """
        分页查询审计方案信息，可带属性过滤
        :param page: 页码
        :param per_page: 每页数量
        :param kwargs: 属性名=属性值
        :return: 分页结果dict
        """
        try:
            query = db_session.query(AuditPlan)
            if kwargs:
                query = query.filter_by(**kwargs)
            total = query.count()
            items = query.offset((page-1)*per_page).limit(per_page).all()
            return {
                'total': total,
                'page': page,
                'per_page': per_page,
                'items': [AuditPlanService.to_dict(p) for p in items]
            }
        except SQLAlchemyError as e:
            return {'msg': str(e), 'error': True}

    @staticmethod
    def add(item):
        """
        新增审计方案，包含外键和唯一性校验
        :param item: dict
        :return: 结果dict
        """
        required = ['project_id', 'plan_name', 'items']
        for f in required:
            if not item.get(f):
                return {'msg': f'{f}为必填项', 'error': True}
        # 外键存在性校验
        project = db_session.query(ProjectInfo).filter_by(id=item['project_id']).first()
        if not project:
            return {'msg': '所属项目不存在', 'error': True}
        # 同项目方案名称唯一
        exists = db_session.query(AuditPlan).filter_by(project_id=item['project_id'], plan_name=item['plan_name']).first()
        if exists:
            return {'msg': '同项目下方案名称已存在', 'error': True}
        try:
            plan = AuditPlan(
                project_id=item['project_id'],
                plan_name=item['plan_name'],
                items=item['items'],
                remark=item.get('remark')
            )
            db_session.add(plan)
            db_session.commit()
            return {'msg': '添加成功', 'item': AuditPlanService.to_dict(plan)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def update(item_id, item):
        """
        更新审计方案，包含外键和唯一性校验
        :param item_id: 方案ID
        :param item: dict
        :return: 结果dict
        """
        try:
            plan = db_session.query(AuditPlan).filter_by(id=item_id).first()
            if not plan:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            # 外键存在性校验
            if 'project_id' in item and item['project_id'] != plan.project_id:
                project = db_session.query(ProjectInfo).filter_by(id=item['project_id']).first()
                if not project:
                    return {'msg': '所属项目不存在', 'error': True}
            # 同项目方案名称唯一
            if 'plan_name' in item and (item['plan_name'] != plan.plan_name or ('project_id' in item and item['project_id'] != plan.project_id)):
                pid = item.get('project_id', plan.project_id)
                exists = db_session.query(AuditPlan).filter_by(project_id=pid, plan_name=item['plan_name']).first()
                if exists:
                    return {'msg': '同项目下方案名称已存在', 'error': True}
            for f in ['project_id', 'plan_name', 'items']:
                if f in item and not item[f]:
                    return {'msg': f'{f}为必填项', 'error': True}
            for k, v in item.items():
                setattr(plan, k, v)
            db_session.commit()
            return {'msg': '更新成功', 'item': AuditPlanService.to_dict(plan)}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def delete(item_id):
        """
        删除审计方案
        :param item_id: 方案ID
        :return: 结果dict
        """
        try:
            plan = db_session.query(AuditPlan).filter_by(id=item_id).first()
            if not plan:
                return {'msg': '未找到', 'item_id': item_id, 'error': True}
            db_session.delete(plan)
            db_session.commit()
            return {'msg': '删除成功', 'item_id': item_id}
        except SQLAlchemyError as e:
            db_session.rollback()
            return {'msg': str(e), 'error': True}

    @staticmethod
    def to_dict(obj):
        """
        ORM对象转dict
        :param obj: AuditPlan对象
        :return: dict
        """
        return {
            'id': obj.id,
            'project_id': obj.project_id,
            'plan_name': obj.plan_name,
            'items': obj.items,
            'remark': obj.remark
        } 