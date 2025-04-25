from flask import Blueprint, jsonify

analytics_bp = Blueprint('analytics_bp', __name__)

@analytics_bp.route('/analytics', methods=['GET'])
def get_analytics():
    return jsonify({"message": "Analytics endpoint is working"})
