from flask import Blueprint, request, jsonify
from app.service.project_info_service import ProjectInfoService

project_info_bp = Blueprint('project_info', __name__)
service = ProjectInfoService()

@project_info_bp.route('/project_info', methods=['GET'])
def list_project_info():
    return jsonify(service.list())

@project_info_bp.route('/project_info', methods=['POST'])
def add_project_info():
    data = request.json
    return jsonify(service.add(data))

@project_info_bp.route('/project_info/<int:item_id>', methods=['PUT'])
def update_project_info(item_id):
    data = request.json
    return jsonify(service.update(item_id, data))

@project_info_bp.route('/project_info/<int:item_id>', methods=['DELETE'])
def delete_project_info(item_id):
    return jsonify(service.delete(item_id)) 