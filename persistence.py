import pyodbc

server = 'tcp:jcooklcs-sqlserver1.database.windows.net,1433'
database = 'jcookLCS-sqldb1'
dbusername = 'sqladmin'
dbpassword = 'Pa$$w0rd!'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + dbusername
    + ';PWD=' + dbpassword)
cursor = cnxn.cursor()

def get_favorite_for_user(username):
    qstring = 'SELECT * FROM UserFavorites where username = \'' + username + '\''
    print(qstring)
    cursor.execute(qstring)
    row = cursor.fetchone()

    if row is None:
        return

    print('row = %r' % (row,))
    return {'username': row[0], 'favorite': row[1]}

def set_favorite_for_user(username, favorite):
    qstring = 'INSERT into dbo.UserFavorites (UserName, Favorite) VALUES (\'' + username + '\', \'' + favorite + '\')'
    print(qstring)
    cursor.execute(qstring)
    cnxn.commit()

def get_all_favorites():
    qstring = 'SELECT * FROM UserFavorites'
    print(qstring)
    cursor.execute(qstring)
    row = cursor.fetchone()

    if row is None:
        return

    favorites = []
    while row:
        favorites.append({'username': row[0], 'favorite': row[1]})
        row = cursor.fetchone()

    return favorites
