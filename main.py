import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS variavel (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL, 
    saldo FLOAT NOT NULL
        )""")
cursor.execute("""
       INSERT INTO variavel
       (titular, saldo) VALUES ('titular', '500') """)

cursor.execute("SELECT * FROM variavel")
contas = cursor.fetchall()
print(contas)

conexao.commit()

# O programa registra o nome escolhido na área de cursor execute INSERT INTO variavel. . 
# Cadastrando o nome escolhido pelo programador. .

# Próxima atividade pendente. . 
# Cadastro com input(".")
