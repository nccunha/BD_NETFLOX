import psycopg2.extras
from passlib.hash import sha256_crypt

#Verifica se existe algum cliente registado com este e-mail
def CLIENTE_EMAIL(email): # procura um cliente com este e-mail se existir devolve true
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor()

        cur.execute("select email"
                    " from cliente_historico_cliente "
                    "where email = %(a)s", {'a' : email})
        x1 = None
        for linha in cur.fetchall():
            x1 = linha
        if x1 is not None:
            return True
        else:
            return False

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#Verifica se as credencias do cliente estão corretas
def CREDENCIAIS_CLIENTE(email, password):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM cliente_historico_cliente WHERE cliente_historico_cliente.email = %(b)s",{'b': email})
        records = cur.fetchall()
        for row in records:
            if(sha256_crypt.verify(password, row[3])):
                return True
            else:
                return False
                cur.close()


        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#Verifica que quem está a tentar entrar é um admin ou nao
def CREDENCIAIS_ADMIN(email,password):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM administrador WHERE administrador.email = %(b)s",{'b': email})
        records = cur.fetchall()
        for row in records:
            if (sha256_crypt.verify(password, row[1])):
                return True
            else:
                return False
                cur.close()


        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def ARTIGO_ID(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * " 
                    "FROM artigos "
                    "WHERE artigos.id = %(b)s",{'b': id})
        x1=None
        for linha in cur.fetchall():
            x1=linha
        if x1 is not None:
            return True
        else:
            return False

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()