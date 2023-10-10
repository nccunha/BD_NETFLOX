import psycopg2.extras
from prettytable import PrettyTable
import datetime

#CLIENTE
def selecionaArtigos():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT id,nome,tipo,preco FROM artigos ORDER BY id")
        artigos = cur.fetchall()  # para todos
        print("\tArtigos encontrados: ")
        i = 1
        for artigo in artigos:
            print("ID: " + str(artigo['id']) + "\t\tNome: " + artigo['nome'] + "\t\tTipo: " + artigo[
                'tipo'] + "\t\tPreço: " + str(artigo['preco']))
            i += 1

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def selecionaArtigo(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * "
                    "FROM artigos "
                    "WHERE artigos.id =%s", [id])

        artigos = cur.fetchall()
        print("Artigos com id " + str(id) + ": ")
        i = 1
        for artigo in artigos:
            print("ID: " + str(artigo['id']) + "\t\tNome: " + artigo['nome'] + "\t\tTipo: " + artigo[
                'tipo'] + "\t\tPreço: " + str(artigo['preco']) +
                  "\t\tTempo Disponível: " + str(artigo['tempo_disp']) + "\t\tProdutor: " + artigo[
                      'produtor'] + "\t\tRealizador: " + artigo['realizador'])
            i += 1

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Preco_Artigo(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT preco "
                    "FROM artigos "
                    "WHERE artigos.id =%s", [id])
        x2 = cur.fetchone()['preco']
        cur.close()
        return x2

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Artigos_disponiveis(id):
    sim = True
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        comando = ("SELECT * FROM artigoalugado WHERE artigoalugado.cliente_historico_cliente_email='{}'")
        cur.execute(comando.format(id))

        for dias in cur.fetchall():
            x1 = dias['data_final']
            x2 = dias['artigos_id']

            if (datetime.datetime.now().date() < (x1)):
                comando2 = ("SELECT * FROM artigos WHERE artigos.id = %s")
                cur.execute(comando2, (x2,))
                i = 0
                for artigo in cur.fetchall():
                    print("ID: " + str(artigo['id']) + "\t\tNome: " + artigo['nome'] + "\t\tTipo: " + artigo[
                        'tipo'])
                    i += 1
                sim = False
        if sim:
            print("Não tem artigos disponíveis")


        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#MENSAGENS CLIENTE
def MENSAGEM_DE(id_cliente):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando = ("SELECT estado FROM leitura  WHERE leitura.cliente_historico_cliente_email='{}'")

        cur.execute(comando.format(id_cliente))

        idx = 0

        for linha in cur.fetchall():

            idx = idx + 1
            x1 = linha['estado']

            if x1 is False:
                t = 'Não lido'
            else:
                t = 'lido'

            print(idx, '. ESTADO ', t, '\n')

        cur.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def MENSAGEM_POR_idx(idx_1, id_cliente):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        COMANDO = ("SELECT * FROM mensagens,leitura  WHERE leitura.cliente_historico_cliente_email = '{}' AND mensagens.id=leitura.mensagens_id")

        cur.execute(COMANDO.format(id_cliente))

        idx = 0
        for linha in cur.fetchall():
            idx = idx + 1
            x3 = linha['id']
            x1 = linha['texto']
            x2 = linha['data']

            if str(idx_1) == str(idx):
                print(idx, '. data da mensagem : ', x2, '\n texto :  ', x1, '\n')
                break

        cur.close()
        return x3

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#INFO CLIENTE
def cliente_nome(email):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando = "SELECT username FROM cliente_historico_cliente WHERE cliente_historico_cliente.email = '{}' "

        cur.execute(comando.format(email))

        nome, = cur.fetchall()

        print(nome[0])

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def CLIENTE_SALDO(email):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT saldo "   
                    "FROM cliente_historico_cliente "
                    "WHERE cliente_historico_cliente.email = %(b)s", {'b': email})

        x1 = cur.fetchone()[0]
        cur.close()
        return x1
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#ALUGA
def COMPRA_POR_ID(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * "  
                    "FROM artigoalugado "
                    "WHERE artigoalugado.id = %(b)s", {'b': id})
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

def TOTAL_ALUGUER(id_carrinho):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        comando = "SELECT preco FROM artigoalugado WHERE artigoalugado.id = {} "
        cur.execute(comando.format(id_carrinho))

        for linha in cur.fetchall():
            x4 = linha[0]

        cur.close()
        return x4
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def CATALGO_CLIENTE():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * "  
                    "FROM artigos ")

        idx = 0
        x = PrettyTable(["idx ", "Nome", "Tipo", "Produtor", "Realizador", "Preço"])
        x.align["idx"] = "l"
        x.align["Nome"] = "l"
        x.align["Tipo"] = "l"
        x.align["Produtor"] = "r"
        x.align["Realizador"] = "r"
        x.align["Preço "] = "r"
        x.padding_width = 1
        for linha in cur.fetchall():
            idx = idx + 1
            x1 = linha['nome']
            x2 = linha['tipo']
            x3 = linha['produtor']
            x4 = linha['realizador']
            x5 = linha['preco']
            x.add_row([idx, x1, x2, x3, x4, x5])
        print(x)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def ARTIGO_POR_idx(idx_1, restricao):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * FROM artigos " + restricao)
        idx = 0
        for linha in cur.fetchall():
            idx = idx + 1
            if str(idx_1) == str(idx):
                x5 = linha['id']
                break

        cur.close()
        return x5
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#HISTORICO CLIENTE
def HISTORICO_COMPRAS(id_cliente):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando = ("SELECT artigos.nome, artigos.tipo, artigoalugado.data_aluguer, artigoalugado.preco" \
                   " FROM artigos, artigoalugado" \
                   " WHERE artigos.id = artigoalugado.artigos_id AND artigoalugado.cliente_historico_cliente_email = '{}'")

        cur.execute(comando.format(id_cliente))
        idx = 0
        x = PrettyTable(["Nome", "Tipo", "data", "preco"])
        x.align["Nome"] = "l"
        x.align["Tipo"] = "l"
        x.align["data"] = "r"
        x.align["Preco"] = "r"

        x.padding_width = 1
        for linha in cur.fetchall():
            idx = idx + 1
            x1 = linha['nome']
            x2 = linha['tipo']
            x3 = linha['data_aluguer']
            x5 = linha['preco']

            x.add_row([x1, x2, x3, x5])
        print(x)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#ADMIN
def ARTIGO_ID(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * "  
                    "FROM artigos_historico_artigos "
                    "WHERE artigos_historico_artigos.id = %(b)s", {'b': id})

        for linha in cur.fetchall():

            x1 = linha['nome']
            x2 = linha ['tipo']
            x4 = linha['preco']
            print(' Nome: ',x1,' Tipo: ',x2,' Preço: ',x4,'\n')

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def selecionaClientes():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT saldo,username,email FROM cliente_historico_cliente ORDER BY username")
        artigos = cur.fetchall()
        print("\tClientes encontrados: ")
        i = 1
        for artigo in artigos:
            print("Saldo: " + str(artigo['saldo']) + "\t\tNome: " + artigo['username'] + "\tEmail: " + str(artigo['email']))
            i += 1

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def PRECO_ANTIGO(id_artigo):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT preco "  
                    "FROM artigos "
                    "WHERE id = %(b)s", {'b': id_artigo})

        x4= cur.fetchone()[0]


        cur.close()
        return x4
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def CLIENTE_SALDO(id_cliente):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT saldo " 
                    "FROM cliente_historico_cliente "
                    "WHERE cliente_historico_cliente.email = %(b)s", {'b': id_cliente})

        x1 = cur.fetchone()[0]
        cur.close()
        return x1
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def CLIENTE_POR_NOME(nome):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * " 
                    "FROM cliente_historico_cliente "
                    "WHERE cliente_historico_cliente.username = %(b)s", {'b': nome})
        idx=0
        for linha in cur.fetchall():
            idx=idx+1
            x1 = linha['username']
            x2 = linha['utilizador_email']

            print(idx,'. Nome: ', x1, ' e_mail: ', x2,  '\n')


        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def MENSAGEM_POR_ID(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * "   
                    "FROM mensagens "
                    "WHERE mensagens.id = %(b)s", {'b': id})
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

def HIS_ALTERACOES():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando = "SELECT *" \
                  " FROM historico_artigos "

        cur.execute(comando)
        idx = 0
        x = PrettyTable(["Data da alteração", "Preço Antigo", "ID da alteração", "ID do artigo"])
        x.align["datamodificacao"] = "l"
        x.align["precoantigo"] = "l"
        x.align["artigos_id"] = "l"
        x.align["id"] = "l"
        x.padding_width = 1
        for linha in cur.fetchall():
            idx = idx + 1
            x1 = linha[0]
            x2 = linha[1]
            x3 = linha[2]
            x4 = linha[3]

            x.add_row([x1, x2, x3, x4])
        print(x)


        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def CATALGO_ADMIN():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * "  
                    "FROM artigos ")

        x = PrettyTable(["id ", "Nome", "Preço", "Tempo disponível", "Tipo","Produtor","Realizador"])
        x.align["id"] = "r"
        x.align["Nome"] = "l"
        x.align["Preço"] = "l"
        x.align["Tempo disponível"] = "r"
        x.align["Tipo"] = "r"
        x.align["Produtor"] = "r"
        x.align["Realizador"] = "r"
        x.padding_width = 1
        for linha in cur.fetchall():
            x1 = linha['id']
            x2 = linha['nome']
            x3 = linha['preco']
            x4 = linha['tempo_disp']
            x5 = linha['tipo']
            x6 = linha ['produtor']
            x7 = linha['realizador']
            x.add_row([x1, x2, x3, x4,x5,x6,x7])
        print(x)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def ADMIN_EMAIL(email):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando = "SELECT email FROM administrador WHERE administrador.email = '{}' "

        cur.execute(comando.format(email))

        email, = cur.fetchall()

        print(email[0])

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#PESQUISA DE ARTIGOS
def PESQUISA_TIPO(nome):
        try:
            conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cur.execute("SELECT * " 
                        "FROM artigos "
                        "WHERE artigos.tipo = %(b)s", {'b': nome})
            idx = 0
            x = PrettyTable(["ID", "Nome", "Tipo", "Preço"])
            x.align["ID"] = "l"
            x.align["Nome"] = "l"
            x.align["Tipo"] = "l"
            x.align["Preço "] = "l"
            x.padding_width = 1
            for linha in cur.fetchall():
                idx = idx + 1
                x1 = linha['id']
                x2 = linha['nome']
                x3 = linha['tipo']
                x4 = linha['preco']
                x.add_row([x1, x2, x3, x4])
            print(x)

            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            if conn is not None:
                conn.close()

def PESQUISA_TITULO(nome):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * "  
                    "FROM artigos "
                    "WHERE artigos.nome = %(b)s", {'b': nome})
        idx = 0
        x = PrettyTable(["ID", "Nome", "Tipo", "Preço"])
        x.align["ID"] = "l"
        x.align["Nome"] = "l"
        x.align["Tipo"] = "l"
        x.align["Preço "] = "l"
        x.padding_width = 1
        for linha in cur.fetchall():
            idx = idx + 1
            x1 = linha['id']
            x2 = linha['nome']
            x3 = linha['tipo']
            x4 = linha['preco']
            x.add_row([x1, x2, x3, x4])
        print(x)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def PESQUISA_REALIZADOR(nome):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * "  
                    "FROM artigos "
                    "WHERE artigos.realizador = %(b)s", {'b': nome})
        idx = 0
        x = PrettyTable(["ID", "Nome", "Tipo", "Preço"])
        x.align["ID"] = "l"
        x.align["Nome"] = "l"
        x.align["Tipo"] = "l"
        x.align["Preço "] = "l"
        x.padding_width = 1
        for linha in cur.fetchall():
            idx = idx + 1
            x1 = linha['id']
            x2 = linha['nome']
            x3 = linha['tipo']
            x4 = linha['preco']
            x.add_row([x1, x2, x3, x4])
        print(x)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def PESQUISA_PRODUTOR(nome):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * " 
                    "FROM artigos "
                    "WHERE artigos.produtor = %(b)s", {'b': nome})
        idx = 0
        x = PrettyTable(["ID", "Nome", "Tipo", "Preço"])
        x.align["ID"] = "l"
        x.align["Nome"] = "l"
        x.align["Tipo"] = "l"
        x.align["Preço "] = "l"
        x.padding_width = 1
        for linha in cur.fetchall():
            idx = idx + 1
            x1 = linha['id']
            x2 = linha['nome']
            x3 = linha['tipo']
            x4 = linha['preco']
            x.add_row([x1, x2, x3, x4])
        print(x)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def PESQUISA_ATORES(nome):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * "  
                    "FROM atores "
                    "WHERE atores.nome = %(b)s", {'b': nome})
        id_artigo = cur.fetchone()[1]
        cur.execute("SELECT * " 
                    "FROM artigos "
                    "WHERE artigos.id = %(b)s", {'b': id_artigo})

        idx = 0
        x = PrettyTable(["ID", "Nome", "Tipo", "Preço"])
        x.align["ID"] = "l"
        x.align["Nome"] = "l"
        x.align["Tipo"] = "l"
        x.align["Preço "] = "l"
        x.padding_width = 1
        for linha in cur.fetchall():
            idx = idx + 1
            x1 = linha['id']
            x2 = linha['nome']
            x3 = linha['tipo']
            x4 = linha['preco']
            x.add_row([x1, x2, x3, x4])
        print(x)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#PESQUISA DE ARTIGOS DISPONÍVEIS
def Artigos_disponiveis_TIPO(id, nome):
    sim = True
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        comando = ("SELECT * FROM artigoalugado WHERE artigoalugado.cliente_historico_cliente_email='{}'")
        cur.execute(comando.format(id))

        for dias in cur.fetchall():
            x1 = dias['data_final']
            x2 = dias['artigos_id']

            if datetime.datetime.now().date() < (x1):
                comando2 = ("SELECT * FROM artigos WHERE artigos.id = %s AND artigos.tipo = %s ")
                cur.execute(comando2, (x2, nome,))
                artigos = cur.fetchall()
                i = 0
                for artigo in artigos:
                    print("ID: " + str(artigo['id']) + "\t\tNome: " + artigo['nome'] + "\t\tTipo: " + artigo[
                        'tipo'])
                    i += 1
            sim = False

        if sim:
            print("Não tem artigos disponíveis")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Artigos_disponiveis_TITULO(id, nome):
    sim = True
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        comando = ("SELECT * FROM artigoalugado WHERE artigoalugado.cliente_historico_cliente_email='{}'")
        cur.execute(comando.format(id))

        for dias in cur.fetchall():
            x1 = dias['data_final']
            x2 = dias['artigos_id']

            if datetime.datetime.now().date() < (x1):
                comando2 = ("SELECT * FROM artigos WHERE artigos.id = %s AND artigos.nome = %s ")
                cur.execute(comando2, (x2, nome,))
                artigos = cur.fetchall()
                i = 0
                for artigo in artigos:
                    print("ID: " + str(artigo['id']) + "\t\tNome: " + artigo['nome'] + "\t\tTipo: " + artigo[
                        'tipo'])
                    i += 1
            sim = False

        if sim:
            print("Não tem artigos disponíveis")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Artigos_disponiveis_REALIZADOR(id, nome):
    sim = True
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        comando = ("SELECT * FROM artigoalugado WHERE artigoalugado.cliente_historico_cliente_email='{}'")
        cur.execute(comando.format(id))

        for dias in cur.fetchall():
            x1 = dias['data_final']
            x2 = dias['artigos_id']

            if datetime.datetime.now().date() < (x1):
                comando2 = ("SELECT * FROM artigos WHERE artigos.id = %s AND artigos.realizador = %s ")
                cur.execute(comando2, (x2, nome,))
                artigos = cur.fetchall()
                i = 0
                for artigo in artigos:
                    print("ID: " + str(artigo['id']) + "\t\tNome: " + artigo['nome'] + "\t\tTipo: " + artigo[
                        'tipo'])
                    i += 1
            sim = False

        if sim:
            print("Não tem artigos disponíveis")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Artigos_disponiveis_PRODUTOR(id, nome):
    sim = True
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        comando = ("SELECT * FROM artigoalugado WHERE artigoalugado.cliente_historico_cliente_email='{}'")
        cur.execute(comando.format(id))

        for dias in cur.fetchall():
            x1 = dias['data_final']
            x2 = dias['artigos_id']

            if datetime.datetime.now().date() < (x1):
                comando2 = ("SELECT * FROM artigos WHERE artigos.id = %s AND artigos.produtor = %s ")
                cur.execute(comando2, (x2, nome,))
                artigos = cur.fetchall()
                i = 0
                for artigo in artigos:
                    print("ID: " + str(artigo['id']) + "\t\tNome: " + artigo['nome'] + "\t\tTipo: " + artigo[
                        'tipo'])
                    i += 1
            sim = False

        if sim:
            print("Não tem artigos disponíveis")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#ATORES
def CATALGO_ATORES(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * "  
                    "FROM atores "
                    "WHERE atores.artigos_id = %(b)s", {'b': id})
        atores =cur.fetchall()
        print("Atores encontrados: ")
        i = 1
        for atores in atores:
            print("ID: " + str(atores['artigos_id']) + "\t\tNome: " + atores['nome'])
            i += 1

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Artigos_disponiveis_ATOR(EMAIL, nome):
    sim = True
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        comando = ("SELECT * FROM artigoalugado WHERE artigoalugado.cliente_historico_cliente_email='{}'")
        cur.execute(comando.format(EMAIL))

        for dias in cur.fetchall():
            x1 = dias['data_final']
            x2 = dias['artigos_id']

            if datetime.datetime.now().date() < (x1):
                comando2 = ("SELECT * FROM artigos,atores WHERE artigos.id = %s AND atores.nome = %s ")
                cur.execute(comando2, (x2, nome,))
                artigos = cur.fetchall()
                i = 0
                for artigo in artigos:
                    print("ID: " + str(artigo['id']) + "\t\tNome: " + artigo['nome'] + "\t\tTipo: " + artigo[
                        'tipo'])
                    i += 1
            sim = False

        if sim:
            print("Não tem artigos disponíveis")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()