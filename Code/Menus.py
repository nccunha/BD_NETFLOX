import Verifica
import Registo
import Opcao
import Procura
import Estatisticas
from passlib.hash import sha256_crypt

def MENU_INICIAL():
    print('_____________|NETFLOX|_____________')
    print('1. Fazer o registo')
    print('2. Fazer o Login ')
    op= eval(input('Digite o numero da opção que deseja: '))
    if op == 1:
        return MENU_REGISTO()
    elif op == 2:
        return MENU_LOGIN()
    else:
        MENU_INICIAL()

def ADMIN_REGISTO():
    print("<<<<<<<<<<Registo admin>>>>>>>>>>")
    EMAIL = input('EMAIL: ')
    if Verifica.CLIENTE_EMAIL(EMAIL):
        ADMIN_REGISTO()
    PASSWORD = input('PASSWORD: ')
    HASH = sha256_crypt.hash(PASSWORD)
    Registo.ADMIN(EMAIL,HASH)
    return EMAIL

def MENU_REGISTO():
    print("<<<<<<<<<<Registo>>>>>>>>>>")
    USERNAME = input('NOME: ')
    EMAIL = input('EMAIL: ')
    if Verifica.CLIENTE_EMAIL(EMAIL):
        print("Este email já está a ser usado")
        MENU_REGISTO()
    PASSWORD = input('PASSWORD: ')
    HASH = sha256_crypt.hash(PASSWORD)
    Registo.CLIENTE(USERNAME,EMAIL,HASH)
    MENU_INICIAL()

def MENU_LOGIN():
    print("<<<<<<<<<<Login>>>>>>>>>>")
    EMAIL = input('EMAIL: ')
    PASSWORD = input('PASSWORD: ')
    if Verifica.CREDENCIAIS_CLIENTE(EMAIL, PASSWORD):
        MENU_CLIENTE(EMAIL)
    if Verifica.CREDENCIAIS_ADMIN(EMAIL, PASSWORD):
        MENU_ADMIN(EMAIL)
    else:
        print('A palavra-chave ou o e-mail estão incorretos')
        MENU_LOGIN()

def MENU_ADMIN(EMAIL):
    print("\nADMIN: ")
    Procura.ADMIN_EMAIL(EMAIL)
    print("""<<<<<<<<<<<<Menu Administrador>>>>>>>>>>>>
    1. Mensagens
    2. Adicionar novo artigo
    3. Editar artigo
    4. Ver estatisticas
    5. Aumentar saldo
    6. Ver todos os artigos
    7. Histórico de alterações
    8. Sair
    """)
    escolha = eval(input("Opção: "))
    if escolha == 1:
        Opcao.mensagens_enviar()
        MENU_ADMIN(EMAIL)
    if escolha == 2:
        Opcao.adicionar_artigo()
        MENU_ADMIN(EMAIL)
    if escolha == 3:
        print('1. Apagar artigo \n2. Corrigir preços\n3. Retornar ao Menu\n')
        ops = eval(input("Opção:"))
        if ops == 2:
            Opcao.corrigir_preco()
            MENU_ADMIN(EMAIL)
        if ops == 1:
            Opcao.eliminar_artigo()
            MENU_ADMIN(EMAIL)
        else:
            MENU_ADMIN(EMAIL)
    if escolha == 4:
        print('1. Ver estatisticas \n2. Retornar ao Menu\n')
        ops = eval(input("Opção:"))
        if ops == 1:
            print('Número total de clientes registados: ', Estatisticas.CLIENTES_TOTAL())
            print('Total de artigos: ', Estatisticas.TOTAL_ARTIGOS())
            print('Valor total de artigos alugados: ', Estatisticas.Total_artigos_alugados())
            print('Total de artigos por tipo: ')
            print('Filmes-', Estatisticas.Total_tipo_filme())
            print('Séries-', Estatisticas.Total_tipo_serie())
            print('Documentários-', Estatisticas.Total_tipo_doc())
            MENU_ADMIN(EMAIL)
        else:
            MENU_ADMIN(EMAIL)
    if escolha == 5:
        Opcao.aumentar_saldo()
        MENU_ADMIN(EMAIL)
    if escolha == 6:
        print('1. Ver todos os artigos \n2.Ver todos os atores\n3. Retornar ao Menu\n')
        ops = eval(input("Opção:"))
        if ops == 1:
            Opcao.todos_artigos()
            print(' <<<Histórico de alterações>>> ')
            Procura.HIS_ALTERACOES()
            MENU_ADMIN(EMAIL)
        if ops == 2:
            Opcao.todos_artigos()
            escolha = eval(input("ID do artigo que prentende ver os atores: "))
            Procura.CATALGO_ATORES(escolha)
        else:
            MENU_ADMIN(EMAIL)
    if escolha == 7:
        Procura.HIS_ALTERACOES()
        MENU_ADMIN(EMAIL)
    if escolha == 8:
        MENU_INICIAL()
    else:
        MENU_ADMIN(EMAIL)

def MENU_CLIENTE(EMAIL):
    print('BEM VINDO,')
    Procura.cliente_nome(EMAIL)
    print('SALDO DISPONÍVEL:', Procura.CLIENTE_SALDO(EMAIL))# imprime o nome do cliente que está a usar o serviço
    print("""\n1.Mensagens\n2.Loja\n3.Artigos disponíveis\n4.Ver Histórico de compras\n5.Logout\n""")
    escolha = eval(input("Opção:"))
    if escolha == 1:
        Opcao.ver_mensagens(EMAIL)
        MENU_CLIENTE(EMAIL)
    if escolha == 2:
        print("""\n1.Listar todos os artigos\n2.Detalhes de um artigo\n3.Pesquisa\n4.Alugar um artigo\n5.Retornar ao Menu\n""")
        loja = eval(input("Opção: "))
        if loja == 1:
            Procura.selecionaArtigos()
            print("\n")
            MENU_CLIENTE(EMAIL)
        if loja == 2:
            Procura.selecionaArtigos()
            print("\nInsira o id do artigo: ")
            id_artigo = eval(input("ID: "))
            Procura.selecionaArtigo(id_artigo)
            MENU_CLIENTE(EMAIL)
        if loja == 3:
            print("""\n1.Pesquisa por tipo\n2.Pesquisa por título\n3.Pesquisa por atores\n4.Pesquisa por realizador\n5.Pesquisa por produtor\n6.Retornar ao Menu\n""")
            pesquisa = eval(input("Opção: "))
            if pesquisa == 1:
                nome = input('Tipo do artigo: ')
                Procura.PESQUISA_TIPO(nome)
            if pesquisa == 2:
                nome = input('Título do artigo: ')
                Procura.PESQUISA_TITULO(nome)
            if pesquisa == 3:
                nome = input('Atores do artigo: ')
                Procura.PESQUISA_ATORES(nome)
            if pesquisa == 4:
                nome = input('Realizador do artigo: ')
                Procura.PESQUISA_REALIZADOR(nome)
            if pesquisa == 5:
                nome = input('Produtor do artigo: ')
                Procura.PESQUISA_PRODUTOR(nome)
            else:
                 MENU_CLIENTE(EMAIL)
        if loja == 4:
            print("Que artigo deseja alugar? ")
            Procura.selecionaArtigos()
            ID_ARTIGO = eval(input("ID: "))
            Opcao.loja(EMAIL, ID_ARTIGO)
            MENU_CLIENTE(EMAIL)
        else:
            MENU_CLIENTE(EMAIL)
    if escolha == 3:
        print(
            """\n1.Listar todos os artigos disponíveis\n2.Pesquisa por tipo\n3.Pesquisa por título\n4.Pesquisa por atores\n5.Pesquisa por realizador\n6.Pesquisa por produtor\n7.Retornar ao Menu\n""")
        pesquisa = eval(input("Opção: "))
        if pesquisa == 1:
            Procura.Artigos_disponiveis(EMAIL)
            print("\n")
            MENU_CLIENTE(EMAIL)
        if pesquisa == 2:
            nome = input('Tipo do artigo: ')
            Procura.Artigos_disponiveis_TIPO(EMAIL, nome)
        if pesquisa == 3:
            nome = input('Título do artigo: ')
            Procura.Artigos_disponiveis_TITULO(EMAIL, nome)
        if pesquisa == 4:
            nome = input('Atores do artigo: ')
            Procura.Artigos_disponiveis_ATOR(EMAIL, nome)
        if pesquisa == 5:
            nome = input('Realizador do artigo: ')
            Procura.Artigos_disponiveis_REALIZADOR(EMAIL, nome)
        if pesquisa == 6:
            nome = input('Produtor do artigo: ')
            Procura.Artigos_disponiveis_PRODUTOR(EMAIL, nome)
        else:
            MENU_CLIENTE(EMAIL)
    if escolha == 4:
        print("""\n1.Listar todas as compras\n2.Saldo total gasto\n3.Saldo gasto por tipo\n4.Retornar ao Menu\n""")
        escolha = eval(input("Opção:"))
        if escolha == 1:
            Procura.HISTORICO_COMPRAS(EMAIL)
            MENU_CLIENTE(EMAIL)
        if escolha == 2:
            Estatisticas.GASTO_TOTAL(EMAIL)
            MENU_CLIENTE(EMAIL)
        if escolha == 3:
            Estatisticas.Total_tipo(EMAIL)
            MENU_CLIENTE(EMAIL)
        if escolha == 4:
            MENU_CLIENTE(EMAIL)
    if escolha == 5:
        MENU_INICIAL()
    else:
        MENU_CLIENTE(EMAIL)

