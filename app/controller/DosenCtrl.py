from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response


def allData():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        return response.success(data, "Response success")
    except Exception as e:
        print(e)
        return response.badReq(e, "Gagal mengambil data")

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id ) | (Mahasiswa.dosen_dua == id))
        
        if not dosen:
            return response.badReq([], 'Dosen not found')
        
        dataMhs = formatMhs(mahasiswa)
        result = detailDosen(dosen, dataMhs)
        
        return response.success(result, "Response success")
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

def formatMhs(data):
    array = []
    
    for i in data:
        array.append(singleDetailMhs(i))
        
    return array

def singleDetailMhs(data):
    data = {
        'id': data.id,
        'nim': data.nim,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat,
    }
    
    return data
    
def detailDosen(dosen, mhs):
    data= {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'nama': dosen.id,
        'phone': dosen.id,
        'alamat': dosen.id,
        'mahasiswa': mhs
    }
    
    return data