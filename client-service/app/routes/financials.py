from flask import Blueprint, jsonify

financials_bp = Blueprint('financials_bp', __name__)

@financials_bp.route('/financials', methods=['GET'])
def get_financials():
    return jsonify({"message": "Financials endpoint is working"})
