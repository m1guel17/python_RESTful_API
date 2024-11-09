from API.mapping.modelMapping import model_mapping
from API.services.model import Model
from API.credentials import CREDENTIALS
from API import db

from flask import jsonify, request
from functools import wraps
import base64

def check_basic_auth(auth_header):
    if not auth_header:
        return False
    try:
        auth_type, encoded_credentials = auth_header.split(" ")
        if auth_type.lower() != "basic":
            return False
        credentials = base64.b64decode(encoded_credentials).decode("utf-8")
        username, password = credentials.split(":")
        return CREDENTIALS.get(username) == password
    except Exception:
        return False

def require_basic_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        print(auth_header)
        if not check_basic_auth(auth_header):
            return jsonify({"error": "Unauthorized access"}), 401
        return f(*args, **kwargs)
    return decorated_function

def getpost(app):
    @app.route('/api', methods=['GET', 'POST', 'PUT'])
    @require_basic_auth
    def api():
        data = request.get_json()
        if request.method == 'GET':
            return Model.request(data)
        elif request.method == 'POST':
            return Model.insert(data)
        elif request.method == 'PUT':
            return Model.insert(data)
        
# def getpost(app):
#     @app.route('/api/query', methods=['GET'])
#     @require_basic_auth
#     def query_data():
#         data = request.get_json()
#         return Model.request(data)
    
#     @app.route('/api/create', methods=['POST'])
#     @require_basic_auth
#     def dynamic_insert():
#         data = request.get_json()
#         return Model.insert(data)