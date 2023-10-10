import psycopg2.extras

def CLIENTES_TOTAL():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT COUNT() "  # vai buscar tudo sobre a linha 
                    "FROM cliente_historico_cliente ")

        for linha in cur.fetchall():
            var = linha[0]

        cur.close()
        return var
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def TOTAL_ARTIGOS():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT COUNT() "  # vai buscar tudo sobre a linha 
                    "FROM artigos ")

        for linha in cur.fetchall():
            var = linha[0]

        return var

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Total_tipo_filme():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT COUNT(*)  "  # vai buscar tudo sobre a linha 
                    "FROM artigos "
                    "Where tipo='filme'")

        for linha in cur.fetchall():
            var = linha[0]

        return var

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Total_tipo_serie():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT COUNT()  "  # vai buscar tudo sobre a linha 
                    "FROM artigos "
                    "Where tipo='serie'")

        for linha in cur.fetchall():
            var = linha[0]

        return var

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Total_tipo_doc():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT COUNT()  "  # vai buscar tudo sobre a linha 
                    "FROM artigos "
                    "Where tipo='documentario'")

        for linha in cur.fetchall():
            var = linha[0]

        return var

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Total_artigos_alugados():
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT COUNT(*)  "  # vai buscar tudo sobre a linha 
                    "FROM artigoalugado ")

        for linha in cur.fetchall():
            var = linha[0]

        return var

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def GASTO_TOTAL(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        comando = ("SELECT sum(preco) FROM artigoalugado WHERE artigoalugado.cliente_historico_cliente_email='{}'")
        cur.execute(comando.format(id))

        x1 = cur.fetchone()[0]
        print("Gasto total: " + str(x1) + "\n")

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def Total_tipo(id):
    try:
        conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        comando1 = "SELECT DISTINCT tipo FROM artigos "
        cur.execute(comando1)
        for l in cur.fetchall():
            var = l[0]
            command=("SELECT sum(artigoalugado.preco) "  
                    "FROM artigoalugado, artigos WHERE artigoalugado.cliente_historico_cliente_email = '{}' AND artigoalugado.artigos_id=artigos.id AND artigos.tipo = '{}'")
            cur.execute(command.format(id, var))
            for linha in cur.fetchall():
                vari = linha[0]
                print(var,' : ',vari)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()