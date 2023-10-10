import Registo
import Atualiza
import Procura
import psycopg2.extras


#ADMIN
def adicionar_artigo():
    #clear()
    print('1. Adicionar um artigo\n'
          '2.Adicionar Atores\n'
          '3. Sair')
    escolha = eval(input('opção: '))
    if escolha == 1:
        NOME= input('Nome do artigo: ')
        DATA=input('Tempo disponivel: ')
        PRECO = eval(input('Preço: '))
        TIPO = input('Tipo: ')
        PRODUTOR = input('Produtor: ')
        REALIZADOR = input('Realizador: ')
        Registo.ARTIGO(NOME,PRECO, DATA,TIPO,PRODUTOR,REALIZADOR)
    if escolha ==2:
        todos_artigos()
        ID = eval(input('ID do artigo: '))
        ATORES=input('Nome do ator: ')
        Registo.ATORES(ATORES,ID)

    if escolha == 3:
        return

def eliminar_artigo():
        Procura.selecionaArtigos()
        id = input('ID do artigo a apagar: ')
        Atualiza.APAGAR_ARTIGO(id)

def corrigir_preco():
     Procura.selecionaArtigos()
     id=input('ID do artigo a corrigir o preço: ')
     #Verifica.ARTIGO_ID(id)
     preco = eval(input('Preço novo para o artigo: '))
     Registo.HISTORICO_ALTERACOES(Procura.PRECO_ANTIGO(id), id)  # primeiro grava o preço anterior e depois é que altera
     Atualiza.CORRIGIR_PRECO(id,preco)

def aumentar_saldo():
    #clear()
    Procura.selecionaClientes()
    id_cliente = ' '
    print('1. Aumentar o saldo de um clinete pesquisando por email\n'
          '2. Aumentar o saldo de todos os clientes\n'
          '3.Sair')
    escolha = eval(input('opção: '))
    if escolha == 3:
        return
    if escolha == 1:
        e_mail_procura = input('e-mail da pessoa: ')

        id_cliente = e_mail_procura
    if escolha == 2:
        assunto = eval(input('Escreva o valor a aumentar: '))  # tbm pode diminuir se o valor for negativo
        try:
            conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cur.execute("SELECT email FROM cliente_historico_cliente ")

            idx = 0
            for linha in cur.fetchall():
                idx = idx + 1

                x2 = linha[0]
                Atualiza.AUMENTA_SALDO(x2,assunto+Procura.CLIENTE_SALDO(x2))
            cur.close()
            return

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    assunto = eval(input('Escreva o valor a aumentar: '))

    Atualiza.AUMENTA_SALDO(id_cliente, assunto + Procura.CLIENTE_SALDO(id_cliente))

def mensagens_enviar():
    #clear()
    Procura.selecionaClientes()
    id_cliente= ' '
    print('1. enviar para um cliente pesquisando por email\n'
          '2. enviar para todos os clientes\n'
          '3. Sair')
    escolha= eval(input('opção: '))
    if escolha == 3:
        return

    if escolha == 1:
        e_mail_procura = input('e-mail da pessoa: ')

        id_cliente = e_mail_procura
    if escolha == 2:
        assunto = input('Escreva a mensagem: ')
        try:
            conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cur.execute("SELECT email FROM cliente_historico_cliente ")


            for linha in cur.fetchall():


                x2 = linha['email']
                Registo.LEITURA(Registo.MENSAGEM(assunto), x2)
            cur.close()
            return

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    assunto=input('Escreva a mensagem: ')
    Registo.LEITURA(Registo.MENSAGEM(assunto),id_cliente)

def todos_artigos():
    Procura.CATALGO_ADMIN()

# MENU DO CLIENTE
def ver_mensagens(id_cliente):
    Procura.MENSAGEM_DE(id_cliente)
    opcao= eval(input('Opção: '))
    #clear()
    id_mensagens = Procura.MENSAGEM_POR_idx(opcao, id_cliente)
    Atualiza.ESTADO_MENSAGEM(id_mensagens, id_cliente)

#LOJA
def lista_artigos():
    Procura.CATALGO_CLIENTE()  # função que mostra todos os artigos
    idx = eval(input(' em que indice está o album que escolheu ? : '))
    # não tem restrição
    return Procura.ARTIGO_POR_idx(idx, ' ')  # devolve o id do artigo que a pessoa escolheu

def loja(EMAIL, id_artigo):
    #clear()
    preco = Procura.Preco_Artigo(id_artigo)
    saldo = Procura.CLIENTE_SALDO(EMAIL)
    print('SALDO: ', saldo)
    print("PREÇO DO ARTIGO: ", preco)

    if saldo - preco >= 0:
        valor = float(preco)
        Registo.ALUGA(EMAIL, id_artigo, preco)
        Atualiza.ALTERA_SALDO(EMAIL, valor * -1)  # retira o dinheiro da conta do cliente
        print('ARTIGO ALUGADO COM SUCESSO\n')

    if preco - saldo >= 0:
        print('NÃO TEM SALDO SUFICIENTE\n')