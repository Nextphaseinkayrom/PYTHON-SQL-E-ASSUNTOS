import sqlite3

conexao = sqlite3.connect("sql_join/informacao.db")
cursor = conexao.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            nome TEXT
            ) 
            """)

cursor.execute("""
          CREATE TABLE IF NOT EXISTS gastos (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          descricao TEXT,
          valor REAL,
          id_categoria INT,
          FOREIGN KEY (id_categoria) REFERENCES categorias(id)
          )
          """)

conexao.commit()


cursor.execute("INSERT INTO categorias (nome) VALUES (?)", ("Alimentacao", ))
cursor.execute("INSERT INTO categorias (nome) VALUES (?)", ("Transporte",))
cursor.execute("INSERT INTO categorias (nome) VALUES (?)", ("Lazer",))

cursor.execute("INSERT INTO gastos (descricao, valor, id_categoria) VALUES (?, ?, ?)", ("Almoço", 25.0, 1))
cursor.execute("INSERT INTO gastos (descricao,valor, id_categoria) VALUES (?, ?, ?)", ("Uber", 18.0, 2))
cursor.execute("INSERT INTO gastos (descricao,valor, id_categoria) VALUES (?, ?, ?)", ("Mercado", 90.0, 1))
cursor.execute("INSERT INTO gastos (descricao, valor, id_categoria) VALUES (?, ?, ?)", ("Ônibus", 6.5, 2))
cursor.execute("INSERT INTO gastos (descricao, valor, id_categoria) VALUES (?,?,?)", ("Hótel", 70.0, 3))

conexao.commit()

pg_menu = int(input("1/2/3//5"))

if pg_menu == 1:
    cursor.execute("""
               SELECT gastos.descricao, categorias.nome, gastos.valor
               FROM gastos
               JOIN categorias ON gastos.id_categoria = categorias.id
               WHERE categorias.nome = 'Transporte'
    """)

    for cada in cursor.fetchall():
       nome, descricao, id_categorias = cada
       print(f"""
       Nome :{nome}
       Descrição:{descricao}
       ID Da Categoria:{id_categorias}""")

elif pg_menu == 2:
    cursor.execute("""
               SELECT gastos.descricao, categorias.nome, gastos.id_categoria
               FROM gastos
               JOIN categorias ON gastos.id_categoria = categorias.id
               WHERE categorias.nome = 'Alimentacao'
               """)

    for cada in cursor.fetchall():
       nome, descricao, id_categorias = cada
       print(f"""
       Nome :{nome}
       Descrição:{descricao}
       ID Da Categoria:{id_categorias}""")

elif pg_menu == 3:
   cursor.execute("""
              SELECT gastos.descricao, categorias.nome, gastos.id_categoria
              FROM gastos
              JOIN categorias ON gastos.id_categoria = categorias.id
              WHERE categorias.nome = 'Lazer'
              """)
   for cada in cursor.fetchall():
       nome, descricao, id_categorias = cada
       print(f"""
       Nome :{nome}
       Descrição:{descricao}
       ID Da Categoria:{id_categorias}""")





