#greetings = [
#    {'lang': 'en', 'phrase': 'Hello'},
#    {'lang': 'es', 'phrase': 'Hola'},
#    {'lang': 'gr', 'phrase': 'Guten tag'},
#    {'lang': 'fr', 'phrase': 'Bonne journee'}
#]
userFavorites = [
    {'username': 'Jason', 'fav': 'vanilla'},
    {'username': 'John', 'fav': 'rocky road'},
    {'username': 'Paul', 'fav': 'strawberry'},
    {'username': 'Ringo', 'fav': 'vanilla'},
    {'username': 'Default', 'fav': 'chocolate'}
]


def get_favorite_for_username(username):
    for userFavorite in userFavorites:
        if userFavorite['username'].lower() == username.lower():
            return userFavorite

#def get_greeting_for_lang(lang):
#    for greeting in greetings:
#        if greeting['lang'] == lang:
#            return greeting

# TODO implement get / put to db