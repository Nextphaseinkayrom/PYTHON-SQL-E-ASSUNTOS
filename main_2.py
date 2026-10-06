# Objetivo cadastrar algum nome ou idade com Input(".").E decorar a memorização do novo assunto/
# Pendente. . .
import sqlite3
import time

def funcao():
 conexao = sqlite3.connect("banco.db")
 cursor = conexao.cursor()

 cursor.execute("""CREATE TABLE IF NOT EXISTS variavel (
       id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       nome TEXT UNIQUE,
       idade NUMBER
            )
       """)
 menu = int(input("""
      --- MENU ---
      1 -- REGISTRO
      2 -- EXIBIÇÃO DE USER'S
      3 -- LOCALIZADOR DE ID'S(DESENVOLVIMENTO)
      4 -- MODIFICADOR
      5 -- DELETADOR
      
      Sua Resposta: """))
       
 
 
 
 
 if menu == 1:
  print("CREATE")
  nome = str(input("Nome:"))
  idade = int(input("Idade: "))
  print("Fazendo processo")
  time.sleep(2.0)
  
  if nome and idade:
   print("Registrando . .")
   cursor.execute("INSERT INTO variavel (nome, idade) VALUES (?,?)",
      (nome, idade))
   conexao.commit()
   return True
  #If's 1 Completo.
 

 
 elif menu == 2:
   
   print("READ ALL")
   time.sleep(2)
   cursor.execute("SELECT * FROM variavel")
   resultado = cursor.fetchall()
   
   if resultado == []:
      print("Não encontramos nenhum úsuario no momento.")
      return True
    
    
   else:
     for inf in resultado:
      id, nome, idade = inf
      print(f"""
    Nome: {nome}
    Idade: {idade}
    ID: {id}""")
     return True
   #If's 2 completo.

 
 elif menu == 3:
   print("FOUNDER")

   procurador = int(input("Digite o id: "))
   if procurador:  
    cursor.execute(
         "SELECT nome FROM variavel WHERE id = ?",
                  (procurador,))
    resultado = cursor.fetchone()
    
    if resultado is None:
     print("Não encontramos. . .")

    else:
      print(f"Encontramos. .\nA pessoa que deseja é {resultado}")
  #If's 3 Completo.
  
 
 elif menu == 4:
     print("UPDATE")
     modificador = int(input("1: Nome\nIdade: 2"))
     
     
     if modificador == 1:
       print("Entrando na área de nomes. .")
       pg_r = int(input("Qual o ID exáto da pessoa?\nNumeros inteiros apenas. "))
       cursor.execute(
       "SELECT nome FROM variavel WHERE id = ?",
       (pg_r,)
       )
       
       resultado = cursor.fetchone()
       if resultado is None:
          print("Não encontramos")  
       
       else:
         print(f"O nome da pessoa é {resultado}?")
         pg_m = input("Ponha o novo nome. .")
         if pg_m:
           cursor.execute(
             "UPDATE variavel SET nome = ? WHERE id = ?",
             (pg_m, pg_r)
             )
           resultadodamod = cursor.fetchone()
           conexao.commit()
           print(f"O novo nome é {resultadodamod}")
           return True
          # 
       
     #If's 4 Completo.



 elif menu == 5:
   print("DELETE")
   pg_d = str(input("Digite o nome da pessoa que deseja remover. . .\nR: "))
   if pg_d:
     cursor.execute(
       "SELECT * FROM variavel WHERE nome = ?",
       (pg_d,))
     resul_2 = cursor.fetchall()
     for cada in resul_2:
      id, nome, idade = cada
     if resul_2 == []:
      print("N/R")

     else:
      pg_c = int(input(f"""
Informações da pessoa:
Id:{id}
Nome: {nome}
Idade: {idade}

Deseja Apagar mesmo? 
1 = Sim/2 = Não

Sua resposta: """))
      if pg_c == 1:
        print("Removendo . . .")
        cursor.execute(
          "DELETE FROM variavel WHERE nome = ?",
            (pg_d,))
        
        conexao.commit()
        
        print("Pessoa removida. . ")
        return True


      else:
       print("Operação sendo desfeita. .")
       return True  





#Delete Pendente. . .

while True:
   True
   if not funcao():
    break