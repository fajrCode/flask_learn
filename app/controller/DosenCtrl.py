from app.model.dosen import Dosen
from app import response, app, db
from flask import request


def allData():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        return response.success(data, "Response success")
    except Exception as e:
        print(e)
        return response.badReq(e, "Gagal mengambil data")

def oneData(id):
    try:
        dosen = Dosen.query.one()
        data = singleObject(dosen)
        return response.success(data, "Response success")
    except Exception as e:
        print(e)
        return response.badReq(e, "Gagal mengambil data")

def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array


def singleObject(data):
    data = {
        "id": data.id,
        "nidn": data.nidn,
        "nama": data.nama,
        "phone": data.phone,
        "alamat": data.alamat,
    }

    return data
