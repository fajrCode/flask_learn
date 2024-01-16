from flask import Blueprint, request
from app.helper import response
from app.controller import DosenCtrl, MhsCtrl, UserCtrl
# from flask_jwt_extended import get_jwt_identity, jwt_required

api = Blueprint("api", __name__, template_folder="..templates")


@api.route("/")
def index():
    return response.successMsg("API ready to use")


# route dosen
@api.route("/dosen", methods=["GET", "POST"])
def dosen():
    if request.method == "GET":
        # if di bawah buat cek headers
        # if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        #     return response.success(dosen, "Response success")
        dosen = DosenCtrl.allData()
        return response.success(dosen, "Response success")
    elif request.method == "POST":
        return DosenCtrl.create()
    else:
        return response.notFound()


@api.route("/dosen/<id>", methods=["GET", "PUT", "DELETE"])
# @jwt_required()
def detailDosen(id):
    if request.method == "GET":
        # print(get_jwt_identity())
        result = DosenCtrl.detail(id)
        return response.success(result, "Response success")
    elif request.method == "PUT":
        return DosenCtrl.edit(id)
    elif request.method == "DELETE":
        return DosenCtrl.delete(id)
    else:
        return response.notFound()


# route mahasiswa
@api.route("/mahasiswa", methods=["GET", "POST"])
def mahasiswa():
    if request.method == "GET":
        mhs = MhsCtrl.allData()
        return response.success(mhs, "Response success")
    elif request.method == "POST":
        return MhsCtrl.create()
    else:
        return response.notFound()


@api.route("/mahasiswa/<id>", methods=["GET", "PUT", "DELETE"])
def detailMhs(id):
    if request.method == "GET":
        result = MhsCtrl.detail(id)
        return response.success(result, "Response success")
    elif request.method == "PUT":
        return MhsCtrl.edit(id)
    elif request.method == "DELETE":
        return MhsCtrl.delete(id)
    else:
        return response.notFound()

@api.route('/register', methods=["POST"])
def register():
    return UserCtrl.register()

@api.route("/login", methods=["POST"])
def login():
    return UserCtrl.login()
     