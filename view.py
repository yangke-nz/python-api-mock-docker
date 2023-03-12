from flask import Flask, render_template, json, Response
import os
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

api = Flask(__name__)
basic_auth = HTTPBasicAuth()

mock_data = './mockdata/'
auth_users = {
    "user1": generate_password_hash("user1pass"), 
    "user2": generate_password_hash("user2pass")
}

@api.route('/')
def home():
    return render_template('index.html')



@api.route('/api/v1/version', methods=['GET'])
def version():
    return json.dumps({"version": "1.0.mock"}),{'content-type':'application/json'}




@api.route('/api/v1/item/<string:id>', methods=['GET'])
@basic_auth.login_required
def items(id):
    try:   
        data = False    
        file = mock_data + id + '_data.json'
        print(id)
        if os.path.exists(file):
            data = json.load(open(file,))
        
        if data:     
            return json.dumps(data),{'content-type':'application/json'}
        else:
            return api.response_class(response=json.dumps({'message':'Not exist ID: ' + id + '.'}),status=500,mimetype="application/json")
    except Exception as e:
        print(str(e))


@basic_auth.verify_password
def verify_password(username, password):
    if username in auth_users and \
            check_password_hash(auth_users.get(username), password):
        return username


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    api.run(debug=True, host='0.0.0.0', port=port)