from flask import Blueprint, jsonify

bp = Blueprint("calendar", __name__)

@bp.route("/today", methods=["GET"])
def get_today():
    return jsonify({
        "date": "2025-07-24",
        "events": [
            { "title": "AI 회의", "time": "10:00" },
            { "title": "백엔드 구조 만들기", "time": "15:00" }
        ]
    })
