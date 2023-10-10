import psycopg2.extras

#ARTIGOS
def APAGAR_ARTIGO(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        comando1 = """SELECT * FROM artigoalugado WHERE artigos_id = %s"""

        comando2 = """DELETE FROM artigos WHERE id = %s"""

        comando4 = """DELETE FROM atores WHERE artigos_id = %s"""

        comando5 = """SELECT * FROM artigos WHERE id = %s"""

        cur.execute(comando5, (id,))

        if cur.rowcount < 1:
            print("ID não existente")

        else:
            cur.execute(comando1, (id,))

            if cur.rowcount < 1:
                cur = conn.cursor()
                cur.execute(comando4, (id,))
                cur.execute(comando2, (id,))
                print("\nArtigo apagado com sucesso")
                conn.commit()

            else:
                print("\nArtigo encontra-se alugado por um cliente")

            conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def CORRIGIR_PRECO(id, preco):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando1 = "UPDATE artigos SET preco = {} WHERE id = {}"

        cur.execute(comando1.format(preco, id))
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#SALDO
def ALTERA_SALDO(email, saldo):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando = "SELECT saldo FROM cliente_historico_cliente WHERE email ='{}'"
        cur.execute(comando.format(email))
        s = cur.fetchone()[0]

        comando1 = "UPDATE cliente_historico_cliente SET saldo = {} WHERE cliente_historico_cliente.email = '{}'"

        cur.execute(comando1.format(s + saldo, email))

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def AUMENTA_SALDO(id_cliente, saldo):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando = "SELECT saldo FROM cliente_historico_cliente WHERE email ='{}'"
        cur.execute(comando.format(id_cliente))
        s = cur.fetchone()[0]

        comando1 = "UPDATE cliente_historico_cliente SET saldo = {} WHERE cliente_historico_cliente.email = '{}'"

        cur.execute(comando1.format(saldo, id_cliente))

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#MENSAGENS
def ESTADO_MENSAGEM(id_mensagens, id_cliente):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando1 = "UPDATE leitura SET estado = {} WHERE leitura.mensagens_id = {} AND leitura.cliente_historico_cliente_email= '{}'"

        cur.execute(comando1.format(True, id_mensagens, id_cliente))
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
