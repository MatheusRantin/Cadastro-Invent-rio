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
        print('Erro, ')

    cur = conn.cursor()
    SQL = f"SELECT nome, email FROM users WHERE email ='{email}' AND senha = '{pwd}'"
    cur.execute(SQL)
    response_database = cur.fetchall()
    print(response_database)
    try:
        response_database[0][1]
        return True
    except IndexError:
        return False
        
    

