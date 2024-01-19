from flask import Blueprint, request, render_template, redirect
from app.helper import response
from app.controller import MhsCtrl, DosenCtrl

Mahasiswa = Blueprint('mahasiswa', __name__, template_folder="..templates")

@Mahasiswa.route("/", methods=["GET", "POST"])
def mahasiswa():
    if request.method == "GET":
        mhs = MhsCtrl.allData()
        return render_template("mahasiswa.html", title="Flask and Jinja", datas=mhs)
    elif request.method == "POST":
        MhsCtrl.create()
        return redirect('/mahasiswa')
    else:
        return response.notFound()
    
@Mahasiswa.route("/add", methods=["GET"])
def addMahasiswa():
    if request.method == "GET":
        nameType = [
            {"type": "text", "name": "nim", "text": "NIM"},
            {"type": "text", "name": "nama", "text": "Nama"},
            {"type": "text", "name": "phone", "text": "No Telepon"},
            {"type": "text", "name": "alamat", "text": "Alamat"},
        ]
        dosenType = [
            {"name": "dosen_satu", "text": "Dosen Pembimbing 1"},
            {"name": "dosen_dua", "text": "Dosen Pembimbing 2"},
        ]
        dosens = DosenCtrl.allData()
    if request.method == "GET":
        return render_template("formMahasiswa.html", title="Flask and Jinja", nameType=nameType, dosens=dosens, dosenType=dosenType)
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