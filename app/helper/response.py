from flask import jsonify, make_response

def success(value, message):
    res = {
        'code': 200,
        'status': 'OK',
        'message': message,
        'data': value
    }
    
    return make_response(jsonify(res)), 200

def successMsg(message):
    res = {
        'code': 200,
        'status': 'OK',
        'message': message
    }
    
    return make_response(jsonify(res)), 200

def successCreated(message):
    res = {
        'code': 201,
        'status': 'OK',
        'message': message
    }
    
    return make_response(jsonify(res)), 201

def badReq(value, message):
    res = {
        'code': 400,
        'status': 'Bad Request',
        'message': message,
        'data': value
    }
    
    return make_response(jsonify(res)), 400

def unAuth(message):
    res = {
        'code': 401,
        'status': 'Unauthorized',
        'message': message
    }
    
    return make_response(jsonify(res)), 400

def notFound():
    res = {
        'code': 404,
        'status': 'Not Found',
        'message': 'Page Not Found'
    }
    
    return make_response(jsonify(res)), 404

def serverError():
    res = {
        'code': 500,
        'status': 'Internal Server Error',
        'message': 'Server Error'
    }
    
    return make_response(jsonify(res)), 500