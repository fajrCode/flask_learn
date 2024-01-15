from app import app, response
from app.controller import DosenCtrl, MhsCtrl
from flask import request

@app.route('/')
def index():
    return response.successMsg('API ready to use')


# route dosen
@app.route('/dosen', methods= ['GET', 'POST'])
def dosen():
    if request.method == 'GET':
        return DosenCtrl.allData()
    elif request.method == 'POST':
        return DosenCtrl.create()
    else:
        return response.notFound()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def detailDosen(id):
    if request.method == 'GET':
        return DosenCtrl.detail(id)
    elif request.method == 'PUT':
        return DosenCtrl.edit(id)
    elif request.method == 'DELETE':
        return DosenCtrl.delete(id)
    else:
        return response.notFound()


#route mahasiswa
@app.route('/mhs', methods=['GET','POST'])
def mahasiswa():
    if request.method == 'GET':
        return MhsCtrl.allData()
    elif request.method == 'POST':
        return MhsCtrl.create()
    else:
        return response.notFound()
    
@app.route('/mhs/<id>', methods=['GET', 'PUT', 'DELETE'])
def detailMhs(id):
    if request.method == 'GET':
        return MhsCtrl.detail(id)
    elif request.method == 'PUT':
        return MhsCtrl.edit(id)
    elif request.method == 'DELETE':
        return MhsCtrl.delete(id)
    else:
        return response.notFound()
    


