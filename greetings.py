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


def get_default_for_username(username):
    for userDefault in userDefaults:
        if userDefault['username'] == username:
            return userDefault

def get_greeting_for_lang(lang):
    for greeting in greetings:
        if greeting['lang'] == lang:
            return greeting

# TODO implement get / put to db