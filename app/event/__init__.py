from flask import Blueprint

event_api = Blueprint('event_api', __name__)

from app.event import event