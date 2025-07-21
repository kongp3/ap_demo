from flask import Blueprint, request, jsonify
from app.service.document_archive_service import DocumentArchiveService

document_archive_bp = Blueprint('document_archive', __name__)
service = DocumentArchiveService()

@document_archive_bp.route('/document_archive', methods=['GET'])
def list_document_archive():
    return jsonify(service.list())

@document_archive_bp.route('/document_archive', methods=['POST'])
def add_document_archive():
    data = request.json
    return jsonify(service.add(data))

@document_archive_bp.route('/document_archive/<int:item_id>', methods=['PUT'])
def update_document_archive(item_id):
    data = request.json
    return jsonify(service.update(item_id, data))

@document_archive_bp.route('/document_archive/<int:item_id>', methods=['DELETE'])
def delete_document_archive(item_id):
    return jsonify(service.delete(item_id)) 