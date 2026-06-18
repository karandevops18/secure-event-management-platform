from flask import Blueprint

events_bp = Blueprint("events", __name__)

@events_bp.route("/events", methods=["GET"])
def get_events():
    return {"message": "Events endpoint working"}, 200