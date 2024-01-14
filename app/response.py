from flask import jsonify, make_response

def success(value, message):
    res = {
        'code': 200,
        'status': 'OK',
        'message': message,
        'data': value
    }
    
    return make_response(jsonify(res)), 200

def badReq(value, message):
    res = {
        'code': 400,
        'status': 'Bad Request',
        'message': message,
        'data': value
    }
    
    return make_response(jsonify(res)), 400