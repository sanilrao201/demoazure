import greetings
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def greeting():
    return jsonify({'greeting': {'phrase': 'Hello guest', 'language': 'en'}})

#GET /greeting?username=Christian HTTP/1.1
#Host: 127.0.0.1:5002
@app.route('/greeting', methods=['GET'])
def get_greeting():
    username = request.args.get('username')
    if username is None:
        username = 'default'

    userdefault = greetings.get_default_for_username(username)
    lang = userdefault['lang']
    greeting = greetings.get_greeting_for_lang(lang)

    return greeting['phrase'] + " " + username

@app.route('/userdefaultgreeting', methods=['POST'])
def set_default_greeting_for_user():
    username = request.args.get('username')
    lang = request.args.get('lang')
    return 'implement POST'

#GET /userdefaultgreeting?username=Hans HTTP/1.1
#Host: 127.0.0.1:5002
@app.route('/userdefaultgreeting', methods=['GET'])
def get_default_greeting_for_user():
    username = request.args.get('username')
    if username is None:
        username = 'default'

    return jsonify(greetings.get_default_for_username(username))

app.run(port='5002')