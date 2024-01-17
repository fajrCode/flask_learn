from flask import Blueprint, request, render_template
from app.helper import response
from app.controller import MhsCtrl

Mahasiswa = Blueprint('mahasiswa', __name__, template_folder="..templates")

@Mahasiswa.route("/", methods=["GET", "POST"])
def mahasiswa():
    if request.method == "GET":
        mhs = MhsCtrl.allData()
        return render_template("mahasiswa.html", title="Flask and Jinja", datas=mhs)
    elif request.method == "POST":
        return MhsCtrl.create()
    else:
        return response.notFound()
    
@Mahasiswa.route("/<id>", methods=["GET"])
def detailMhs(id):
    return MhsCtrl.detail(id)
    
@Mahasiswa.route("/edit/<id>", methods=["GET", "POST"])
def editMhs(id):
    if request.method == "GET":
        return "Form Edit Data"
    elif request.method == "POST":
        return MhsCtrl.edit(id)
    else:
        return "404 Not Found"
    
@Mahasiswa.route("/delete/<id>", methods=["GET"])
def deleteMhs(id):
    return MhsCtrl.delete(id)