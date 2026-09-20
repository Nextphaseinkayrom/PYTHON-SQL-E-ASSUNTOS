# Objetivo cadastrar algum nome ou idade com Input(".")
# Pendente. . .
import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
       CREATE TABLE IF NOT EXISTS variavel(
       id NOT NULL INTEGER,
       nome TEXT
            )""")

cursor.execute("INSERT variavel(kayrom) VALUES (?)")

cursor.fetchall()

resultado = cursor.commit()

print(resultado)