import psycopg2

conn = psycopg2.connect(
                        database='LivrariaMarialva',
                        host="localhost",
                        port=5432,
                        user='postgres',
                        password='003217'
                        )
def getUser(user):
    try:
        email = user['email']
        pwd = user['password']
    except:
        print('Erro, valores invalidos ')

    cur = conn.cursor()
    SQL = f"SELECT email FROM users WHERE email ='{email}' AND senha = '{pwd}'"
    cur.execute(SQL)
    response_database = cur.fetchall()
    try:
        if response_database[0][0] == email:
            return True
    except IndexError:
        return False

def getNameUser(email):
    cur= conn.cursor()
    SQL = f"SELECT nome FROM users WHERE email = '{email}';"
    cur.execute(SQL)
    response_database = cur.fetchall()
    try:
        response_database = response_database[0][0]

        return response_database
    except IndexError:
        return "Erro"