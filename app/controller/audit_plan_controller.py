from flask import Blueprint, request, jsonify
from app.service.audit_plan_service import AuditPlanService

audit_plan_bp = Blueprint('audit_plan', __name__)
service = AuditPlanService()

@audit_plan_bp.route('/audit_plan', methods=['GET'])
def list_audit_plan():
    return jsonify(service.list())

@audit_plan_bp.route('/audit_plan', methods=['POST'])
def add_audit_plan():
    data = request.json
    return jsonify(service.add(data))

@audit_plan_bp.route('/audit_plan/<int:item_id>', methods=['PUT'])
def update_audit_plan(item_id):
    data = request.json
    return jsonify(service.update(item_id, data))

@audit_plan_bp.route('/audit_plan/<int:item_id>', methods=['DELETE'])
def delete_audit_plan(item_id):
    return jsonify(service.delete(item_id)) 