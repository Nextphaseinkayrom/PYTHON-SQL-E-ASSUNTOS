# Objetivo cadastrar algum nome ou idade com Input(".").E decorar a memorização do novo assunto/
# Pendente. . .
import sqlite3

def funcao():
 conexao = sqlite3.connect("banco.db")
 cursor = conexao.cursor()

 cursor.execute("""CREATE TABLE IF NOT EXISTS variavel (
       id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       nome TEXT,
       idade NUMBER
            )
       """)
 menu = int(input("Digite. ."))
 
 
 if menu == 1:
  print("Área de Registro")
  nome = str(input("Nome:"))
  idade = int(input("Idade: "))
  
  if nome and idade:
   print("Registrando . .")
   cursor.execute("INSERT INTO variavel (nome, idade) VALUES (?,?)",
      (nome, idade))
   conexao.commit()
   return True
 
 
 elif menu == 2:
   cursor.execute("SELECT * FROM variavel")
   resultado = cursor.fetchall()
   for inf in resultado:
    id, nome, idade = inf
    print(f"""
    Nome: {nome}
    Idade: {idade}
    ID: {id}""")
   return True


 elif menu == 3:
   procurador = input("Digite o nome: ")
   


while True:
   True
   if not funcao():
    break