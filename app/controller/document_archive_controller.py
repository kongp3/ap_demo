from flask import Blueprint, request, jsonify
from app.service.document_archive_service import DocumentArchiveService

document_archive_bp = Blueprint('document_archive', __name__)

@document_archive_bp.route('/document_archive', methods=['GET'])
def list_document_archive():
    """
    查询所有文书归档信息
    """
    return jsonify(DocumentArchiveService.list())

@document_archive_bp.route('/document_archive/<int:item_id>', methods=['GET'])
def get_document_archive_by_id(item_id):
    """
    按主键查询文书归档信息
    """
    return jsonify(DocumentArchiveService.get_by_id(item_id))

@document_archive_bp.route('/document_archive/query', methods=['POST'])
def query_document_archive_by_attr():
    """
    按属性查询文书归档信息，返回列表
    """
    data = request.json or {}
    return jsonify(DocumentArchiveService.query_by_attr(**data))

@document_archive_bp.route('/document_archive/page', methods=['POST'])
def paginate_document_archive():
    """
    分页查询文书归档信息
    """
    data = request.json or {}
    page = data.get('page', 1)
    per_page = data.get('per_page', 10)
    filters = {k: v for k, v in data.items() if k not in ['page', 'per_page']}
    return jsonify(DocumentArchiveService.paginate(page, per_page, **filters))

@document_archive_bp.route('/document_archive', methods=['POST'])
def add_document_archive():
    """
    新增文书归档
    """
    data = request.json
    return jsonify(DocumentArchiveService.add(data))

@document_archive_bp.route('/document_archive/<int:item_id>', methods=['PUT'])
def update_document_archive(item_id):
    """
    更新文书归档
    """
    data = request.json
    return jsonify(DocumentArchiveService.update(item_id, data))

@document_archive_bp.route('/document_archive/<int:item_id>', methods=['DELETE'])
def delete_document_archive(item_id):
    """
    删除文书归档
    """
    return jsonify(DocumentArchiveService.delete(item_id)) 