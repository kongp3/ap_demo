from flask import Blueprint, request, jsonify
from app.service.report_setting_service import ReportSettingService

report_setting_bp = Blueprint('report_setting', __name__)
service = ReportSettingService()

@report_setting_bp.route('/report_setting', methods=['GET'])
def list_report_setting():
    return jsonify(service.list())

@report_setting_bp.route('/report_setting', methods=['POST'])
def add_report_setting():
    data = request.json
    return jsonify(service.add(data))

@report_setting_bp.route('/report_setting/<int:item_id>', methods=['PUT'])
def update_report_setting(item_id):
    data = request.json
    return jsonify(service.update(item_id, data))

@report_setting_bp.route('/report_setting/<int:item_id>', methods=['DELETE'])
def delete_report_setting(item_id):
    return jsonify(service.delete(item_id)) 