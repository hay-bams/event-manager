from flask import Blueprint

center_api = Blueprint('center_api', __name__)

from app.center import center, errors

