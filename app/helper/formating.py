def dataDosen(datas):
    array = []

    for i in datas:
        array.append(dosen(i))

    return array

def dosen(data):
    data = {
        "id": data.id,
        "nidn": data.nidn,
        "nama": data.nama,
        "phone": data.phone,
        "alamat": data.alamat,
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


def dataMhs(data):
    array = []
    
    for i in data:
        array.append(mhs(i))
        
    return array

def mhs(data):
    data = {
        'id': data.id,
        'nim': data.nim,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat,
    }
    
    return data
  