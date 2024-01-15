from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import db
from app.helper import response
from flask import request
from app.helper.formating import dataDosen, dataMhs, detailDosen


def allData():
    try:
        data = Dosen.query.all()
        result = dataDosen(data)
        return result
    except Exception as e:
        print(e)
        return response.serverError()



def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter(
            (Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id)
        )

        if not dosen:
            return response.badReq([], "Data tidak ditemukan")

        mhs = dataMhs(mahasiswa)
        result = detailDosen(dosen, mhs)

        return response.success(result, "Response success")
    except Exception as e:
        print(e)
        return response.serverError()


def create():
    try:
        nidn = request.form.get("nidn")
        nama = request.form.get("nama")
        phone = request.form.get("phone")
        alamat = request.form.get("alamat")

        dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosens)
        db.session.commit()

        return response.successCreated("Data berhasil di tambahkan")
    except Exception as e:
        print(e)
        return response.serverError()


def edit(id):
    try:
        nidn = request.form.get("nidn")
        nama = request.form.get("nama")
        phone = request.form.get("phone")
        alamat = request.form.get("alamat")

        dosen = Dosen.query.filter_by(id=id).first()

        dosen.nidn = nidn
        dosen.nama = nama
        dosen.phone = phone
        dosen.alamat = alamat

        db.session.commit()

        return response.successCreated("Data berhasil diperbaharui")

    except Exception as e:
        print(e)
        return response.serverError()


def delete(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()

        if not dosen:
            return response.badReq([], "Data tidak ditemukan")

        db.session.delete(dosen)
        db.session.commit()

        return response.successMsg("Berhasil menghapus data")

    except Exception as e:
        print(e)
        return response.serverError()
