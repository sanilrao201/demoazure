import icfavorites
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def greeting():
    return "Welcome to the favorite ice cream tracker 2000!"

# GET /favorite?username=Paul HTTP/1.1
# Host: 0.0.0.0:5002
@app.route('/favorite', methods=['GET'])
def get_favorite():
    username = request.args.get('username')
    if username is None:
        username = 'Default'

    userFavorite = icfavorites.get_favorite_for_username(username)
    if userFavorite is None:
        return "User: " + username + " is not on record."

    favorite = userFavorite['fav']

    return favorite + " is " + username + "'s favorite"

# POST /favorite?username=Paul&fave=Chocolate HTTP/1.1
# Host: 0.0.0.0:5002
@app.route('/favorite', methods=['POST'])
def set_favorite_for_user():
    username = request.args.get('username')
    fave = request.args.get('fave')
    return 'implement POST: ' + username + "/" + fave


app.run(port='5002')