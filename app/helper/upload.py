from werkzeug.utils import secure_filename
from app.config import uploadConfig
# from app import app
from flask import request
from app.helper import response
import uuid
import os


def uploadFile():
    try:
        if 'file' not in request.files:
            return response.badReq([], 'File tidak tersedia')
        
        file = request.files["file"]
        
        if file.filename == '':
            return response.badReq([], 'File tidak tersedia')
        
        if file and uploadConfig.allowFIle(file.filename):
            uid = uuid.uuid4
            filename = secure_filename(file.filename)
            renameFile = "Flask-"+str(uid)+filename
            
            # file.save(os.path.join(app.config["UPLOAD_FOLDER"], renameFile))
            return renameFile
        else:
            return response.badReq([], 'file type not allowed')
            
    except Exception as e:
        print(e)
        return response.serverError()