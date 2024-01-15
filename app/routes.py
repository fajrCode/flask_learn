from app import app, response
from app.controller import DosenCtrl
from flask import request

@app.route('/')
def index():
    return 'Hello Flask'

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