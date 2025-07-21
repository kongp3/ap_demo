from flask import Blueprint, request, jsonify
from app.service.project_member_service import ProjectMemberService

project_member_bp = Blueprint('project_member', __name__)
service = ProjectMemberService()

@project_member_bp.route('/project_member', methods=['GET'])
def list_project_member():
    return jsonify(service.list())

@project_member_bp.route('/project_member', methods=['POST'])
def add_project_member():
    data = request.json
    return jsonify(service.add(data))

@project_member_bp.route('/project_member/<int:item_id>', methods=['PUT'])
def update_project_member(item_id):
    data = request.json
    return jsonify(service.update(item_id, data))

@project_member_bp.route('/project_member/<int:item_id>', methods=['DELETE'])
def delete_project_member(item_id):
    return jsonify(service.delete(item_id)) 