from flask import Blueprint, request, jsonify
from app.service.project_info_service import ProjectInfoService

project_info_bp = Blueprint('project_info', __name__)

@project_info_bp.route('/project_info', methods=['GET'])
def list_project_info():
    """
    查询所有项目信息
    """
    return jsonify(ProjectInfoService.list())

@project_info_bp.route('/project_info/<int:item_id>', methods=['GET'])
def get_project_info_by_id(item_id):
    """
    按主键查询项目信息
    """
    return jsonify(ProjectInfoService.get_by_id(item_id))

@project_info_bp.route('/project_info/query', methods=['POST'])
def query_project_info_by_attr():
    """
    按属性查询项目信息，返回列表
    """
    data = request.json or {}
    return jsonify(ProjectInfoService.query_by_attr(**data))

@project_info_bp.route('/project_info/page', methods=['POST'])
def paginate_project_info():
    """
    分页查询项目信息
    """
    data = request.json or {}
    page = data.get('page', 1)
    per_page = data.get('per_page', 10)
    filters = {k: v for k, v in data.items() if k not in ['page', 'per_page']}
    return jsonify(ProjectInfoService.paginate(page, per_page, **filters))

@project_info_bp.route('/project_info', methods=['POST'])
def add_project_info():
    """
    新增项目信息
    """
    data = request.json
    return jsonify(ProjectInfoService.add(data))

@project_info_bp.route('/project_info/<int:item_id>', methods=['PUT'])
def update_project_info(item_id):
    """
    更新项目信息
    """
    data = request.json
    return jsonify(ProjectInfoService.update(item_id, data))

@project_info_bp.route('/project_info/<int:item_id>', methods=['DELETE'])
def delete_project_info(item_id):
    """
    删除项目信息
    """
    return jsonify(ProjectInfoService.delete(item_id)) 