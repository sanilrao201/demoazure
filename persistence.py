import pyodbc
import os

def build_sql_constr():
    sqlstr = os.environ.get('SQLCONNSTR_icecreamdbconnstr', "SQLCONNSTR_icecreamdbconnstr variable does not exist")
    sqlstrarr = sqlstr.split(";")

    sqlstrmap = {}
    for string in sqlstrarr:
        if string is not '':
            key = string.split('=')[0]
            val = string.split('=')[1]
            sqlstrmap[key] = val

    #TODO whitespace is trimmed here on windows
    server = sqlstrmap['Server']
    database = sqlstrmap['Initial Catalog']
    dbusername = sqlstrmap['User ID']
    dbpassword = sqlstrmap['Password']

    return 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + dbusername + ';PWD=' + dbpassword


#cnxn = pyodbc.connect(
#    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + dbusername
#    + ';PWD=' + dbpassword)


def get_favorite_for_user(username):
    qstring = 'SELECT * FROM UserFavorites where username = \'' + username + '\''
    print(qstring)

    cnxn = pyodbc.connect(build_sql_constr())
    cursor = cnxn.cursor()

    cursor.execute(qstring)
    row = cursor.fetchone()

    if row is None:
        return

    print('row = %r' % (row,))
    return {'username': row[0], 'favorite': row[1]}

def set_favorite_for_user(username, favorite):
    qstring = 'INSERT into dbo.UserFavorites (UserName, Favorite) VALUES (\'' + username + '\', \'' + favorite + '\')'
    print(qstring)

    cnxn = pyodbc.connect(build_sql_constr())
    cursor = cnxn.cursor()
    cursor.execute(qstring)
    cnxn.commit()

def get_all_favorites():
    qstring = 'SELECT * FROM UserFavorites'
    print(qstring)

    cnxn = pyodbc.connect(build_sql_constr())
    cursor = cnxn.cursor()
    cursor.execute(qstring)
    row = cursor.fetchone()

    if row is None:
        return

    favorites = []
    while row:
        favorites.append({'username': row[0], 'favorite': row[1]})
        row = cursor.fetchone()

    return favorites
