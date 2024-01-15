from app import app
from app.helper import response
from app.controller import DosenCtrl, MhsCtrl
from flask import request, render_template


@app.route("/")
def index():
    # return response.successMsg('API ready to use')
    return render_template("index.html", title="Flask and Jinja")


# route dosen
@app.route("/dosen", methods=["GET", "POST"])
def dosen():
    if request.method == "GET":
        # return DosenCtrl.allData()
        dosen = DosenCtrl.allData()
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return response.success(dosen, "Response success")

        return render_template("dosen.html", title="Flask and Jinja", datas=dosen)
    elif request.method == "POST":
        return DosenCtrl.create()
    else:
        return response.notFound()


@app.route("/dosen/<id>", methods=["GET", "PUT", "DELETE"])
def detailDosen(id):
    if request.method == "GET":
        return DosenCtrl.detail(id)
    elif request.method == "PUT":
        return DosenCtrl.edit(id)
    elif request.method == "DELETE":
        return DosenCtrl.delete(id)
    else:
        return response.notFound()


# route mahasiswa
@app.route("/mahasiswa", methods=["GET", "POST"])
def mahasiswa():
    if request.method == "GET":
        # return MhsCtrl.allData()
        mhs = MhsCtrl.allData()

        return render_template("mahasiswa.html", title="Flask and Jinja", datas=mhs)
    elif request.method == "POST":
        return MhsCtrl.create()
    else:
        return response.notFound()


@app.route("/mhs/<id>", methods=["GET", "PUT", "DELETE"])
def detailMhs(id):
    if request.method == "GET":
        return MhsCtrl.detail(id)
    elif request.method == "PUT":
        return MhsCtrl.edit(id)
    elif request.method == "DELETE":
        return MhsCtrl.delete(id)
    else:
        return response.notFound()
