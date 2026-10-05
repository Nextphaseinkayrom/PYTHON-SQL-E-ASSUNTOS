import sqlite3



#Oque é necessário fazer de primeira? E de segunda?
# Primeiro precisa Fazer com que o programa NÃO ACEITE EMAIL REPETIDO
# O nome é aceitável mais o email caso seja repetido, recuse e mande a mensagem
# "Olha não pode por que repetiu"


def func():
 conexao = sqlite3.connect("bank.db")
 cursor = conexao.cursor()   
 
 cursor.execute("""
      CREATE TABLE IF NOT EXISTS variavel (
      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      nome TEXT,
      email TEXT UNIQUE
      )
      """)

 nome_p = str(input("Digite seu Nome: "))
 email_p = input("Digite seu Email: ")


 conexao.commit()

 if "@gmail.com" in email_p:
  try:
   cursor.execute("INSERT INTO variavel (nome, email) VALUES (?,?)",
               (nome_p, email_p,))
   resultado = cursor.fetchall()
   for cada in resultado:
    nome, email = resultado
    print("""
         Nome da pessoa {nome}
         Email da pessoa {email}""")
   print("Cadastrado")
   conexao.commit()
  except sqlite3.IntegrityError:
   print("Ponha outro Email.")

 else:
    print("Onde está a báse do Email?")

