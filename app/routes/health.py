from flask import Blueprint, jsonify, current_app

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok",
                   database_url_in_config = current_app.config.get('SQLALCHEMY_DATABASE_URI')
                   ), 200