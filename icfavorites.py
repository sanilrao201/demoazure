import persistence

def get_favorite_for_username(username):
    return persistence.get_favorite_for_user(username)

def set_favorite_for_username(username, favorite):
    # TODO get username
    # if null
    return persistence.set_favorite_for_user(username, favorite)

    # if no null update

def get_all_favorites():
    return persistence.get_all_favorites()
