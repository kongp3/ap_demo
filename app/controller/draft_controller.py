from flask import Blueprint, request, jsonify
from app.service.draft_service import save_audit_draft, get_first_draft, get_draft_details
from app.util.database import get_db
from datetime import datetime

draft_bp = Blueprint('draft', __name__, url_prefix='/api/draft')


@draft_bp.route('/save', methods=['POST'])
def save_draft():
    """
    保存审计底稿接口
    """
    data = request.get_json()

    # 验证必要字段
    required_fields = [
        "company_name", "status", "matter",
        "name", "code", "operator",
        "source", "model"
    ]

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing_fields)}"
        }), 400

    # 可选字段处理
    data.setdefault("focus", "")
    data.setdefault("draft_id", None)

    db = next(get_db())
    try:
        draft = save_audit_draft(db, data)
        return jsonify({
            "message": "Draft saved successfully",
            "draft_id": draft.id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@draft_bp.route('/query', methods=['GET'])
def query_draft():
    """
    查询审计底稿接口
    """
    db = next(get_db())
    try:
        draft = get_first_draft(db)

        if not draft:
            return jsonify({
                "message": "No drafts found for the given company"
            }), 404

        return jsonify({
            "id": draft.id,
            "company_name": draft.company_name,
            "status": draft.status,
            "matter": draft.matter,
            "name": draft.name,
            "code": draft.code,
            "focus": draft.focus,
            "operator": draft.operator,
            "draft_id": draft.draft_id,
            "source": draft.source,
            "model": draft.model,
            "create_date": draft.create_time.strftime("%Y-%m-%d"),
            "update_date": draft.update_time.strftime("%Y-%m-%d")
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@draft_bp.route('/detail/<int:draft_id>', methods=['GET'])
def draft_detail(draft_id):
    """
    获取底稿详细信息
    """
    db = next(get_db())
    try:
        details = get_draft_details(db, draft_id)

        if not details or not details["main_draft"]:
            return jsonify({
                "message": f"No draft found with ID: {draft_id}"
            }), 404

        # 格式化主底稿信息
        main_draft = details["main_draft"]
        main_data = {
            "id": main_draft.id,
            "company_name": main_draft.company_name,
            "status": main_draft.status,
            "matter": main_draft.matter,
            "name": main_draft.name,
            "code": main_draft.code,
            "focus": main_draft.focus,
            "operator": main_draft.operator,
            "source": main_draft.source,
            "model": main_draft.model,
            "create_time": main_draft.create_time.isoformat(),
            "update_time": main_draft.update_time.isoformat()
        }

        # 格式化引用的底稿
        referenced = []
        for ref in details["referenced_drafts"]:
            referenced.append({
                "id": ref.id,
                "name": ref.name,
                "code": ref.code,
                "operator": ref.operator,
                "create_time": ref.create_time.isoformat()
            })

        # 格式化引用当前底稿的其他底稿
        referencing = []
        for ref in details["referencing_drafts"]:
            referencing.append({
                "id": ref.id,
                "name": ref.name,
                "code": ref.code,
                "operator": ref.operator,
                "create_time": ref.create_time.isoformat()
            })

        return jsonify({
            "main_draft": main_data,
            "referenced_drafts": referenced,
            "referencing_drafts": referencing
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500