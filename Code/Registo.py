import psycopg2
import psycopg2.extras
import Verifica
import random
import Procura
import datetime

def ADMIN(email, password):

    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO administrador(email,password) "
            "VALUES(%s,%s)",
            (email,password))
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def CLIENTE(username, email, password):

    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO cliente_historico_cliente(saldo,username,email,password) "
            "VALUES(%s,%s,%s,%s)",
            (20,username,email,password))
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def ARTIGO(nome,preco,tempo_disp,tipo,produtor,realizador):
   pre_ID = random.randint(0, 1000)

   while Verifica.ARTIGO_ID(pre_ID):
       pre_ID = random.randint(0, 1000)
   id = pre_ID
   try:
       conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
       cur = conn.cursor()

       cur.execute(
           "INSERT INTO artigos(id, nome,preco,tempo_disp,tipo,produtor,realizador) "
           "VALUES(%s,%s,%s,%s,%s,%s,%s)",
        (id, nome, preco, tempo_disp, tipo, produtor, realizador))
       conn.commit()
       cur.close()

   except (Exception, psycopg2.DatabaseError) as error:
       print(error)
   finally:
       if conn is not None:
           conn.close()

def ALUGA(email, id_artigo, preco):
    pre_ID = random.randint(0, 1000)

    while Procura.COMPRA_POR_ID(pre_ID):
        pre_ID = random.randint(0, 1000)
    id = pre_ID
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor()

        comando = "SELECT * FROM artigos WHERE id = %s"
        cur.execute(comando, (id_artigo,))
        dias = cur.fetchone()[6]

        data_aluguer = datetime.datetime.now().date()
        data_final = data_aluguer + datetime.timedelta(days=dias)

        comando2 = "INSERT INTO artigoalugado(id, preco, data_aluguer, artigos_id, cliente_historico_cliente_email, data_final) VALUES(%s,%s,%s,%s,%s,%s)"
        cur.execute(comando2, (id, preco, data_aluguer, id_artigo, email, data_final,))

        print("Artigo disponível até dia " + str(data_final))


        conn.commit()
        cur.close()
        return id

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def HISTORICO_ALTERACOES(preco,id):
    pre_ID = random.randint(0, 1000)
    id_alteracao = pre_ID
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO historico_artigos(datamodificacao, precoantigo,artigos_id,id) "
            "VALUES(CURRENT_TIMESTAMP,%s,%s,%s)",
            (preco, id, id_alteracao))

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#MENSAGENS
def MENSAGEM(assunto):
    pre_ID = random.randint(0, 1000)

    while Procura.MENSAGEM_POR_ID(pre_ID):
        pre_ID = random.randint(0, 1000)
    id = pre_ID
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO mensagens(id,texto,data) "
            "VALUES(%s,%s,CURRENT_TIMESTAMP)",
            (id, assunto))

        conn.commit()
        cur.close()
        return id
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def LEITURA(ID_MENSAGENS,ID_CLIENTE):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO leitura(estado, mensagens_id,cliente_historico_cliente_email) "
            "VALUES(False,%s,%s)",
            (ID_MENSAGENS, ID_CLIENTE))
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#ATORES
def ATORES(nome,artigos_id):

    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO atores(nome,artigos_id) "
            "VALUES(%s,%s)",
            (nome,artigos_id))
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()