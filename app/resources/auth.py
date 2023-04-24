from flask_restful import Resource, marshal
from app.models.models import User
from app import request_api, db
from app.schemas import user_field
import jwt
import datetime
from flask import current_app


class Login(Resource):
    def post(self):
        payload = request_api.only(["username", "password"])
        
        username = payload["username"]
        password = payload["password"]
        
        user = User.query.filter_by(username=username).first()
        
        if not user and not user.compare_password(password):
            return {"Message": "Credenciais estão incorretas."}, 404
        
        data = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=10)
        }
        
        token = jwt.encode(data, current_app.config["SECRET_KEY"])
        
        return {"access_token": token}
    

class Register(Resource):
    def post(self):
        payload = request_api.only(["username", "password"])
        
        username = payload["username"]
        password = payload["password"]
        
        user = User(username, password)
        
        db.session.add(user)
        db.session.commit()
        
        return marshal(user, user_field, "user")
