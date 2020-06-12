from flask import Flask, request, jsonify

app = Flask(__name__)

greetings = [
    {'lang': 'en', 'phrase': 'Hello'},
    {'lang': 'es', 'phrase': 'Hola'},
    {'lang': 'gr', 'phrase': 'Guten tag'},
    {'lang': 'fr', 'phrase': 'Bonne journée'}
]
userDefaults = [
    {'username': 'Jason', 'lang': 'en'},
    {'username': 'Jose', 'lang': 'es'},
    {'username': 'Hans', 'lang': 'gr'},
    {'username': 'Christian', 'lang': 'fr'},
    {'username': 'default', 'lang': 'en'}
]


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

    userdefault = get_default_for_username(username)
    lang = userdefault['lang']
    greeting = get_greeting_for_lang(lang)

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

    return jsonify(get_default_for_username(username))


def get_default_for_username(username):
    for userDefault in userDefaults:
        if userDefault['username'] == username:
            return userDefault

def get_greeting_for_lang(lang):
    for greeting in greetings:
        if greeting['lang'] == lang:
            return greeting




app.run(port='5002')