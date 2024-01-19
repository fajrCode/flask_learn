from flask import Blueprint, request, render_template,redirect
from app.helper import response
from app.controller import DosenCtrl
# from flask_jwt_extended import jwt_required, get_jwt_identity

Dosen = Blueprint("dosen", __name__)


@Dosen.route("/", methods=["GET", "POST"])
def dosen():
    if request.method == "GET":
        dosen = DosenCtrl.allData()
        return render_template("dosen.html", title="Flask and Jinja", datas=dosen)
    elif request.method == "POST":
        DosenCtrl.create()
        return redirect('/dosen')
    else:
        return response.notFound()


@Dosen.route("/add", methods=["GET"])
def addDosen():
    if request.method == "GET":
        nameType = [
            {"type": "text", "name": "nidn", "text": "NIDN"},
            {"type": "text", "name": "nama", "text": "Nama"},
            {"type": "text", "name": "phone", "text": "No Telepon"},
            {"type": "text", "name": "alamat", "text": "Alamat"},
            {"type": "file", "name": "gambar", "text": "Foto Profile"},
        ]
    if request.method == "GET":
        return render_template("formDosen.html", title="Flask and Jinja", nameType=nameType)
    else:
        return response.notFound()


@Dosen.route("/<id>", methods=["GET"])
# @jwt_required()
def detailDosen(id):
    return DosenCtrl.detail(id)


@Dosen.route("/edit/<id>", methods=["GET", "POST"])
def editDosen(id):
    if request.method == "GET":
        return "Form Edit Dosen"
    elif request.method == "POST":
        return DosenCtrl.edit(id)
    else:
        return "404 Not Found"


@Dosen.route("/delete/<id>", methods=["GET"])
def deleteDosen(id):
    return DosenCtrl.delete(id)
