ALLOWED_EXTENTIONS = set(['png', 'jpg', 'jpeg'])

def allowFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS