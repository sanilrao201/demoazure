import icfavorites
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def greeting():
    print('Welcome')
    #return "Welcome to the favorite ice cream tracker 2000! \n" + icfavorites.get_all_favorites().__str__()
    return "Welcome to the favorite ice cream tracker 2000! \n"

# GET /favorite?username=Paul HTTP/1.1
# Host: 0.0.0.0:5002
@app.route('/favorite', methods=['GET'])
def get_favorite():
    username = request.args.get('username')
    if username is None:
        username = 'Default'

    print('Getting favorite for: ' + username)
    userfavorite = icfavorites.get_favorite_for_username(username)
    if userfavorite is None:
        return "User: " + username + " is not on record."

    favorite = userfavorite['favorite']

    return favorite + " is " + username + "'s favorite"

# POST /favorite?username=Paul&favorite=Chocolate HTTP/1.1
# Host: 0.0.0.0:5002
@app.route('/favorite', methods=['POST'])
def set_favorite_for_user():
    username = request.args.get('username')
    favorite = request.args.get('favorite')
    icfavorites.set_favorite_for_username(username, favorite)

    return 'complete'

#app.run(port='80')
