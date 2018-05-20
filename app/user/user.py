from flask import request
from flask import jsonify
from app import db
from app.user import user_api
from app.models import User
from app.exception import ValidationError
from flask_restful import Resource
from app.user import errors


class Signup(Resource):
    def post(self):
        new_user = User()
        new_user.import_data(request.form)

        user = User.query.filter_by(username=request.form['username']).first()
        if user:
            return errors.error_response(400, 'user already exist')

        new_user.set_password_hash(new_user.password)

        db.session.add(new_user)
        db.session.commit()

        token = new_user.encode_token()

        return {
            'status': 'True',
            'message': 'User successfully signed up',
            'token': str(token)
        }, 201


class Signin(Resource):
    def post(self):
        try:
            user = User.query.filter_by(username=request.form['username']).first()

            if not user:
                return jsonify({'message': 'invalid username'})

            if not user.verify_password(request.form['password']):
                return jsonify({'message': 'invalid password'})

            token = user.encode_token()

            return {
                'status': 'True',
                'message': 'User successfully signed in',
                'token': str(token)
            }, 201
        except KeyError as error:
            raise ValidationError('Invalid user, missing ' + error.args[0])

user_api.add_resource(Signup, '/user/signup')
user_api.add_resource(Signin, '/user/signin')
