from flask import Blueprint, send_from_directory
import os

portal_bp = Blueprint("portal", __name__, url_prefix="/portal")
STATIC_PORTAL_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "portal")

@portal_bp.route("/")
def index():
    return send_from_directory(STATIC_PORTAL_DIR, "index.html")