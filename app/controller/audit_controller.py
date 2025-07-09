from flask import Blueprint, request, jsonify
from app.service.audit_service import save_audit_data, get_audit_by_company_name, get_customer_detail_by_audit_id
from app.util.database import get_db

audit_bp = Blueprint('audit', __name__, url_prefix='/api/audit')


@audit_bp.route('/save', methods=['POST'])
def save_audit():
    data = request.get_json()

    # 验证必要字段
    required_fields = ["company_name", "process", "conclusion", "customers"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # 验证客商数据
    for i, customer in enumerate(data["customers"]):
        if "customer_name" not in customer or not customer["customer_name"]:
            return jsonify({"error": f"Missing customer_name in customer index {i}"}), 400

    # 保存数据
    db = next(get_db())
    try:
        audit_id = save_audit_data(db, data)
        return jsonify({
            "message": "Audit data saved successfully",
            "audit_id": audit_id
        }), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500


@audit_bp.route('/query/by_company', methods=['GET'])
def query_by_customer():
    """
    根据客商名称查询审计结果
    """
    company_name = request.args.get('company_name')
    if not company_name:
        return jsonify({"error": "Missing required parameter: company_name"}), 400

    db = next(get_db())
    try:
        results = get_audit_by_company_name(db, company_name)
        if not results:
            return jsonify({"message": "No audit results found for the given company name"}), 404

        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@audit_bp.route('/query/by_audit_id', methods=['GET'])
def query_by_audit_id():
    """
    根据审计ID查询客商详情
    """
    audit_id = request.args.get('audit_id')
    if not audit_id:
        return jsonify({"error": "Missing required parameter: audit_id"}), 400

    try:
        audit_id = int(audit_id)
    except ValueError:
        return jsonify({"error": "Invalid audit_id format. Must be an integer"}), 400

    db = next(get_db())
    try:
        result = get_customer_detail_by_audit_id(db, audit_id)
        if not result:
            return jsonify({"message": f"No audit details found for audit_id: {audit_id}"}), 404

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500