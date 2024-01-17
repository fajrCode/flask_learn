from flask import Blueprint, render_template, request
from app.helper import response
from app.controller import DosenCtrl
# from flask_jwt_extended import jwt_required, get_jwt_identity

dosen = Blueprint("dosen", __name__, render_template)

# route dosen
@dosen.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # return DosenCtrl.allData()
        dosen = DosenCtrl.allData()
        return render_template("dosen.html", title="Flask and Jinja", datas=dosen)
    elif request.method == "POST":
        return DosenCtrl.create()
    else:
        return response.notFound()


# @dosen.route("/<id>", methods=["GET", "PUT", "DELETE"])
# @jwt_required()
# def detailDosen(id):
#     if request.method == "GET":
#         print(get_jwt_identity())
#         return DosenCtrl.detail(id)
#     elif request.method == "PUT":
#         return DosenCtrl.edit(id)
#     elif request.method == "DELETE":
#         return DosenCtrl.delete(id)
#     else:
#         return response.notFound()

