import mysql.connector

__cnx = None

def get_connection():
    global __cnx
    if not __cnx:
        __cnx = mysql.connector.connect(user='root', password='shraddha',
                                      host='127.0.0.1',
                                      database='vendorma')


    return __cnx
