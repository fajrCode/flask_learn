from flask import Blueprint, request
from app.helper import response
from app.controller import DosenCtrl, MhsCtrl
# from flask_jwt_extended import jwt_required, get_jwt_identity

Api = Blueprint('api', __name__, template_folder="..templates")

@Api.route('/')
def index():
    return response.successMsg('API ready to use')

@Api.route('/dosen')
def dosen():
    if request.method == "GET":
        # if dibawah untuk mengambil headers
        # if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        dosen = DosenCtrl.allData()
        return response.success(dosen, "Response success")
    elif request.method == "POST":
        return DosenCtrl.create()
    else:
        return response.notFound()
    
@Api.route("/dosen/<id>", methods=["GET", "PUT", "DELETE"])
# @jwt_required()
def detailDosen(id):
    if request.method == "GET":
        # print(get_jwt_identity())
        return DosenCtrl.detail(id)
    elif request.method == "PUT":
        return DosenCtrl.edit(id)
    elif request.method == "DELETE":
        return DosenCtrl.delete(id)
    else:
        return response.notFound()
    
# mahasiswa route
@Api.route("/mahasiswa", methods=["GET", "POST"])
def mahasiswa():
    if request.method == "GET":
        mhs = MhsCtrl.allData()
        return response.success(mhs, "Response success")
    elif request.method == "POST":
        return MhsCtrl.create()
    else:
        return response.notFound()
    
@Api.route("/mahasiswa/<id>", methods=["GET", "PUT", "DELETE"])
def detailMhs(id):
    if request.method == "GET":
        return MhsCtrl.detail(id)
    elif request.method == "PUT":
        return MhsCtrl.edit(id)
    elif request.method == "DELETE":
        return MhsCtrl.delete(id)
    else:
        return response.notFound()