from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response
from flask import request
from app.helper.formating import dataDosen, dataMhs, detailDosen


def allData():
    try:
        data = Dosen.query.all()
        result = dataDosen(data)
        return response.success(result, "Response success")
    except Exception as e:
        print(e)
        return response.badReq(e, "Gagal mengambil data")

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter(
            (Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id)
        )

        if not dosen:
            return response.badReq([], "Dosen not found")

        mhs = dataMhs(mahasiswa)
        result = detailDosen(dosen, mhs)

        return response.success(result, "Response success")
    except Exception as e:
        print(e)
        return response.badReq(e, "Gagal mengambil data")

def create():
    nidn = request.form.get("nidn")
    nama = request.form.get("nama")
    phone = request.form.get("phone")
    alamat = request.form.get("alamat")

    dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
