from app.user import user_api

@user_api.route('/user')
def user():
  return 'i am a user'