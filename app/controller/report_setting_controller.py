from flask import Blueprint, request, jsonify
from app.service.report_setting_service import ReportSettingService

report_setting_bp = Blueprint('report_setting', __name__)

@report_setting_bp.route('/report_setting', methods=['GET'])
def list_report_setting():
    """
    查询所有入报设定信息
    """
    return jsonify(ReportSettingService.list())

@report_setting_bp.route('/report_setting/<int:item_id>', methods=['GET'])
def get_report_setting_by_id(item_id):
    """
    按主键查询入报设定信息
    """
    return jsonify(ReportSettingService.get_by_id(item_id))

@report_setting_bp.route('/report_setting/query', methods=['POST'])
def query_report_setting_by_attr():
    """
    按属性查询入报设定信息，返回列表
    """
    data = request.json or {}
    return jsonify(ReportSettingService.query_by_attr(**data))

@report_setting_bp.route('/report_setting/page', methods=['POST'])
def paginate_report_setting():
    """
    分页查询入报设定信息
    """
    data = request.json or {}
    page = data.get('page', 1)
    per_page = data.get('per_page', 10)
    filters = {k: v for k, v in data.items() if k not in ['page', 'per_page']}
    return jsonify(ReportSettingService.paginate(page, per_page, **filters))

@report_setting_bp.route('/report_setting', methods=['POST'])
def add_report_setting():
    """
    新增入报设定
    """
    data = request.json
    return jsonify(ReportSettingService.add(data))

@report_setting_bp.route('/report_setting/<int:item_id>', methods=['PUT'])
def update_report_setting(item_id):
    """
    更新入报设定
    """
    data = request.json
    return jsonify(ReportSettingService.update(item_id, data))

@report_setting_bp.route('/report_setting/<int:item_id>', methods=['DELETE'])
def delete_report_setting(item_id):
    """
    删除入报设定
    """
    return jsonify(ReportSettingService.delete(item_id)) 