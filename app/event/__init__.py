from flask import Blueprint
from flask_restful import Api

event_bp = Blueprint('event_bp', __name__)
event_api = Api(event_bp)

from app.event import event, errors