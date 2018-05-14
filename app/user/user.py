from flask import request
from app import db
from app.user import user_api
from app.models import User
from app.exception import ValidationError
from app.user import errors

@user_api.route('/user/signup', methods = ['POST'])
def signup():
  new_user = User()
  new_user.import_data(request.form)
  
  user = User.query.filter_by(username=request.form['username']).first()
  if user:
    return errors.error_response(500, 'user already exist')

  db.session.add(new_user)
  db.session.commit()
  return ''

@user_api.route('/user/sigin')
def signin():
  return 'i am a user'