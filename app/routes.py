from app import app
from app.controller import DosenCtrl

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/dosen', methods= ['GET'])
def dosen():
    return DosenCtrl.allData() 