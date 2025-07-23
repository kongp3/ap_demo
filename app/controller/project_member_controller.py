from flask import Blueprint, request, jsonify
from app.service.project_member_service import ProjectMemberService

project_member_bp = Blueprint('project_member', __name__)

@project_member_bp.route('/project_member', methods=['GET'])
def list_project_member():
    """
    查询所有项目成员信息
    """
    return jsonify(ProjectMemberService.list())

@project_member_bp.route('/project_member/<int:item_id>', methods=['GET'])
def get_project_member_by_id(item_id):
    """
    按主键查询项目成员信息
    """
    return jsonify(ProjectMemberService.get_by_id(item_id))

@project_member_bp.route('/project_member/query', methods=['POST'])
def query_project_member_by_attr():
    """
    按属性查询项目成员信息，返回列表
    """
    data = request.json or {}
    return jsonify(ProjectMemberService.query_by_attr(**data))

@project_member_bp.route('/project_member/page', methods=['POST'])
def paginate_project_member():
    """
    分页查询项目成员信息
    """
    data = request.json or {}
    page = data.get('page', 1)
    per_page = data.get('per_page', 10)
    filters = {k: v for k, v in data.items() if k not in ['page', 'per_page']}
    return jsonify(ProjectMemberService.paginate(page, per_page, **filters))

@project_member_bp.route('/project_member', methods=['POST'])
def add_project_member():
    """
    新增项目成员
    """
    data = request.json
    return jsonify(ProjectMemberService.add(data))

@project_member_bp.route('/project_member/<int:item_id>', methods=['PUT'])
def update_project_member(item_id):
    """
    更新项目成员
    """
    data = request.json
    return jsonify(ProjectMemberService.update(item_id, data))

@project_member_bp.route('/project_member/<int:item_id>', methods=['DELETE'])
def delete_project_member(item_id):
    """
    删除项目成员
    """
    return jsonify(ProjectMemberService.delete(item_id)) 