from flask import Blueprint

user_api =  Blueprint('user_api', __name__)

from app.user import user, errors
