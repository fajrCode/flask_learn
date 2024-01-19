from werkzeug.utils import secure_filename
from app import app
from app.config import uploadConfig
from flask import request
from app.helper import response
import os


def uploadFile():
    try:
        if 'gambar' not in request.files:
            return response.badReq([], 'File tidak tersedia')
            # return "file not in request.files"
        
        file = request.files["gambar"]
        
        if file.filename == '':
            return response.badReq([], 'File tidak tersedia')
            # return "file.name kosong"
        
        if file and uploadConfig.allowFile(file.filename):
            filename = secure_filename(file.filename)
            renameFile = "Flask-"+filename
            
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], renameFile))
            return renameFile
        else:
            return response.badReq([], 'file type not allowed')
            # return "gagal"
            
    except Exception as e:
        print(e)
        return response.serverError()