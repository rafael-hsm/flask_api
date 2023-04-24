from functools import wraps
from flask_restful import request
import jwt
from flask import current_app
from app.models.models import User


from functools import wraps
from flask import request, current_app
import jwt


def jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[0]

        if not token:
            return {'message': 'Token de autenticação ausente.'}, 401

        try:
            decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(decoded['id'])
        except:
            return {'message': 'Token de autenticação inválido.'}, 401

        return func(current_user=current_user, *args, **kwargs)

    return wrapper
