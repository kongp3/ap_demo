from flask import Blueprint, request, jsonify
from app.service.audit_plan_service import AuditPlanService

audit_plan_bp = Blueprint('audit_plan', __name__)

@audit_plan_bp.route('/audit_plan', methods=['GET'])
def list_audit_plan():
    """
    查询所有审计方案信息
    """
    return jsonify(AuditPlanService.list())

@audit_plan_bp.route('/audit_plan/<int:item_id>', methods=['GET'])
def get_audit_plan_by_id(item_id):
    """
    按主键查询审计方案信息
    """
    return jsonify(AuditPlanService.get_by_id(item_id))

@audit_plan_bp.route('/audit_plan/query', methods=['POST'])
def query_audit_plan_by_attr():
    """
    按属性查询审计方案信息，返回列表
    """
    data = request.json or {}
    return jsonify(AuditPlanService.query_by_attr(**data))

@audit_plan_bp.route('/audit_plan/page', methods=['POST'])
def paginate_audit_plan():
    """
    分页查询审计方案信息
    """
    data = request.json or {}
    page = data.get('page', 1)
    per_page = data.get('per_page', 10)
    filters = {k: v for k, v in data.items() if k not in ['page', 'per_page']}
    return jsonify(AuditPlanService.paginate(page, per_page, **filters))

@audit_plan_bp.route('/audit_plan', methods=['POST'])
def add_audit_plan():
    """
    新增审计方案
    """
    data = request.json
    return jsonify(AuditPlanService.add(data))

@audit_plan_bp.route('/audit_plan/<int:item_id>', methods=['PUT'])
def update_audit_plan(item_id):
    """
    更新审计方案
    """
    data = request.json
    return jsonify(AuditPlanService.update(item_id, data))

@audit_plan_bp.route('/audit_plan/<int:item_id>', methods=['DELETE'])
def delete_audit_plan(item_id):
    """
    删除审计方案
    """
    return jsonify(AuditPlanService.delete(item_id)) 