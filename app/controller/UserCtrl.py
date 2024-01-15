from app.model.user import User
from app.helper import response
from app.helper.formating import dataUser
from app import db
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime


def register():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")

        if password != confirmPassword:
            return response.badReq([], "Maaf password yang anda masukkan tidak sama")

        newUser = User(name=name, email=email)
        newUser.setPassword(password)

        db.session.add(newUser)
        db.session.commit()

        return response.successCreated("Berhasil registrasi")
    except Exception as e:
        print(e)
        return response.serverError()


def login():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            return response.badReq([], "Maaf user tidak ditemukan")

        if not user.verifyPassword(password):
            return response.unAuth("Maaf password yang anda masukkan salah")
        
        data= dataUser(user)
        
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)
        
        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        
        result = {"data": data, "access_token": access_token, "refresh_token": refresh_token}
            
        return response.success(result, "Yeay anda berhasil login")
    except Exception as e:
        print(e)
        return response.serverError()
