from app.model.mahasiswa import Mahasiswa
from app.model.dosen import Dosen
from app import response, db
from app.helper.formating import dataMhs, detailMhs, dosen
from flask import request


def allData():
    try:
        data = Mahasiswa.query.all()

        if not data:
            return response.badReq([], "Data not Found")

        result = dataMhs(data)

        return response.success(result, "Response Success")
    except Exception as e:
        print(e)
        return response.serverError()


def detail(id):
    try:
        mhs = Mahasiswa.query.filter_by(id=id).first()
        if not mhs:
            return response.badReq([], "Data tidak ditemukan")


        if not mhs.dosen_satu:
            dosen1 = None
        else:
            dosen_satu = Dosen.query.filter_by(id=mhs.dosen_satu).first()
            dosen1 = dosen(dosen_satu)

        if not mhs.dosen_dua:
            dosen2 = None
        else:
            dosen_dua = Dosen.query.filter_by(id=mhs.dosen_dua).first()
            dosen2 = dosen(dosen_dua)


        result = detailMhs(mhs, dosen1, dosen2)

        return response.success(result, "Response success")

    except Exception as e:
        print(e)
        return response.serverError()


def create():
    try:
        nim = request.form.get('nim')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')
        dosen_satu = request.form.get('dosen_satu')
        dosen_dua = request.form.get('dosen_dua')
        
        mhs = Mahasiswa(nim = nim, nama = nama, phone= phone, alamat=alamat, dosen_satu = dosen_satu, dosen_dua= dosen_dua)
        
        db.session.add(mhs)
        db.session.commit()
        
        return response.successCreated('Berhasil menambahkan data mahasiswa')
        
    except Exception as e:
        print(e)
        return response.serverError()

def edit(id):
    return 'hi'

def delete(id):
    return 'hi'


