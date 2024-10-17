import psycopg2

conn = psycopg2.connect(
                        database='PatrimonioPrefeitura',
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
    SQL = f"SELECT email FROM usuarios WHERE email ='{email}' AND senha = '{pwd}'"
    cur.execute(SQL)
    response_database = cur.fetchall()
    try:
        if response_database[0][0] == email:
            return True
    except IndexError:
        return False

def getNameUser(email):
    cur= conn.cursor()
    SQL = f"SELECT nome FROM usuarios WHERE email = '{email}';"
    cur.execute(SQL)
    response_database = cur.fetchall()
    try:
        response_database = response_database[0][0]

        return response_database
    except IndexError:
        return "Erro"

def getInfoItems(local, modelo):
    cur = conn.cursor() 
    SQL= f"SELECT SUM(quantidade) FROM items WHERE modelo = '{modelo}' AND localizacao = '{local}';"
    cur.execute(SQL)
    response_db = cur.fetchall()
    return response_db

def getLocais():
    cur = conn.cursor()
    SQL ='''
       SELECT l.id AS local_id,  -- Pega o ID do local
       l.nome AS local_nome,
       COALESCE(SUM(CASE WHEN i.nome = 'Impressoras' THEN il.quantidade END), 0) AS quantidade_impressora,
       COALESCE(SUM(CASE WHEN i.nome = 'Computadores' THEN il.quantidade END), 0) AS quantidade_computador,
       COALESCE(SUM(CASE WHEN i.nome = 'Monitores' THEN il.quantidade END), 0) AS quantidade_monitor
        FROM locais l
        LEFT JOIN itens_locais il ON l.id = il.local_id
        LEFT JOIN itens i ON il.item_id = i.id
        GROUP BY l.id, l.nome;  -- Agrupar também pelo ID do local


        '''
    cur.execute(SQL)
    dados = cur.fetchall()
    return dados
    
def getIdLocais():
    cur = conn.cursor()
    SQL = "SELECT id, nome FROM locais"
    cur.execute(SQL)
    response = cur.fetchall()
    return response

def getIdItems():
    cur = conn.cursor()
    SQL = "SELECT id, nome FROM itens"
    cur.execute(SQL)
    response = cur.fetchall()
    return response

def registerItem_locais(id_local, id_item, quantidade):
    cur = conn.cursor()
    SQL = f"INSERT INTO itens_locais VALUES(DEFAULT, '{id_item}', '{id_local}', {quantidade}) "
    cur.execute(SQL)
    conn.commit()
    return True