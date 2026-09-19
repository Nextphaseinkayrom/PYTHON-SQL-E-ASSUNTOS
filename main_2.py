import sqlite3

conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()

cursor.execute("""
       CREATE TABLE pessoa(
       nome TEXT
       
       )""")
nome = input("Nome: ")
cursor.execute(
       "INSERT INTO pessoa (nome) VALUES (?)")
cursor.execute("SELECT * FROM pessoa")

resultado = cursor.fetchall()

print(resultado)

