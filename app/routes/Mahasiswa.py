from flask import Blueprint, request, render_template
from app.controller import MhsCtrl
from app.helper import response

mahasiswa = Blueprint("mahasiswa", __name__, template_folder="..templates")

# route mahasiswa
@mahasiswa.route("/mahasiswa", methods=["GET", "POST"])
def mahasiswa():
    if request.method == "GET":
        # return MhsCtrl.allData()
        mhs = MhsCtrl.allData()

        return render_template("mahasiswa.html", title="Flask and Jinja", datas=mhs)
    elif request.method == "POST":
        return MhsCtrl.create()
    else:
        return response.notFound()

# @mahasiswa.route("/mhs/<id>", methods=["GET", "PUT", "DELETE"])
# def detailMhs(id):
#     if request.method == "GET":
#         return MhsCtrl.detail(id)
#     elif request.method == "PUT":
#         return MhsCtrl.edit(id)
#     elif request.method == "DELETE":
#         return MhsCtrl.delete(id)
#     else:
#         return response.notFound()
