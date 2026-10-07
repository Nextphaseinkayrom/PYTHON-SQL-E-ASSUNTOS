#Oque é necessário fazer de primeira? E de segunda?
# Primeiro precisa Fazer com que o programa NÃO ACEITE email REPETIDO
# O nome é aceitável mais o email caso seja repetido, recuse e mande a mensagem
# "Olha não pode por que repetiu"
# E mostrar os resultados.
def func():
 while True:
  import sqlite3
  conexao = sqlite3.connect("bank.db")
  cursor = conexao.cursor()
 
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS variavel (
      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      nome TEXT,
      email TEXT UNIQUE
      )
      """)
  print("""
   1- C
   2- R
   3- U
   4- D
   5- EXIT""")
  menu = int(input(" R: "))
  if menu == 1:

   nome_p = str(input("Digite seu Nome: "))
   email_p = input("Digite seu Email: ")


   conexao.commit()

   if "@gmail.com" in email_p:
    try:
     cursor.execute("INSERT INTO variavel (nome, email) VALUES (?,?)",
               (nome_p, email_p,))
     conexao.commit()
     print("Cadastrado")
    except sqlite3.IntegrityError:
     print("Ponha outro Email.")

   else:
    print("Onde está a báse do Email?")
# Create completo.

  elif menu == 2:
   cursor.execute("SELECT * FROM variavel")
   resultado = cursor.fetchall()
   for inf in resultado:
    id, nome, email = inf
    print(f"""
    ID: {id}
    NAME: {nome}
    EMAIL: {email}""")
#Read completo.

  elif menu == 3:
   pg_em = input("Email da pessoa?")
   if pg_em:
    cursor.execute("SELECT * FROM variavel WHERE email = ?",
                   (pg_em,))
    resultado = cursor.fetchall()

    print(resultado)
    pg_c = int(input("Deseja alterar mesmo?"))
    if pg_c == 1 :
     pg_c_2 = input("Qual seria o email da pessoa?")
     if "@gmail.com" in pg_c_2:
      cursor.execute("UPDATE variavel SET email = ? WHERE email = ? ",
                     (pg_c_2, pg_em))

      conexao.commit()




func()