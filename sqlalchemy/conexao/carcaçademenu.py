from sqlalchemy import  Integer, String, select, update
from sqlalchemy.orm import  DeclarativeBase, mapped_column, Mapped
import time


from banco import SessionLocal, engine


class Base(DeclarativeBase):
    pass

class Usuarios(Base):
    __tablename__ = "tabela"

    id: Mapped[int] = mapped_column(Integer,  primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=True)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
Base.metadata.create_all(engine)
def cadastro():
   nome = str(input("Digite seu Nome: "))
   idade = int(input("Digite seu Idade: "))
   usuario = Usuarios(idade=idade, nome=nome)
   with SessionLocal() as sessao:
      print("Abrindo sessão. . . ./")
      sessao.add(usuario)
      sessao.commit()
      print(f"Novo Registro\nNome:{usuario.nome}\nIdade:{usuario.idade}")
   

#Exibir
def exibir():
 localizador = str(input("Digite seu nome\nA/S: "))
 
 with SessionLocal() as sessao:
    usuario = sessao.scalars(select(Usuarios).where(Usuarios.nome == localizador)).first()

    if usuario is None:
        print("Seu nome infelizmente não foi encontrado nos registro de banco de dados. . . ")
    
    else:
        print(f"Resultado encontrado\nNome: {usuario.nome}") 

def atualizar():
   with SessionLocal() as sessao:
      atualizar = int(input("1 -- Nome\n2 -- Idade\nA/S: "))
      if atualizar == 1:
       atualizar_nome = str(input("Digite o nome da pessoa: "))
       verificacao_nome = sessao.scalars(select(Usuarios).where(Usuarios.nome == atualizar_nome)).first()
       if verificacao_nome is None:
         print("Sem resultado encontrado")
       else:
         print(f"Entrando na área da coluna de: {verificacao_nome.nome}")
         novo_nome = str(input("Digite novo nome: "))
         sessao.execute(update(Usuarios).where(Usuarios.nome == atualizar_nome).values(nome=novo_nome))
         print("Feito.")
         sessao.commit()
      elif atualizar == 2:
       verificacao_numero = input("Digite o Nome da pessoa: ")
       verificacar_numero = sessao.scalars(select(Usuarios).where(Usuarios.nome == verificacao_numero)).first()
      if verificacar_numero is None:
         print("Não encontramos nenhum registro")
      else:
         print(f"Nome: {verificacar_numero.nome} Idade: {verificacar_numero.idade}")
         idade_nova = int(input("Qual a nova idade: "))
         sessao.execute(update(Usuarios).where(Usuarios.nome == verificacao_numero).values(idade=idade_nova))
         sessao.commit()
      

def menu():
   menu = int(input("""------ MENU ------
    1 -- Cadastrar
    2 -- Exibir
    3 -- Atualizar
    4 -- Apagar
    A/S: """))

   if menu == 1:
      print("Entrando á area de cadastro. . ")
      time.sleep(2)
      cadastro()
   elif menu == 2:
      print("Entrando na área de Exibição. .")
      time.sleep(2)
      exibir()
   elif menu == 3:
     print("Entrando na área de Update")
     time.sleep(2)
     atualizar()
      
   else:
      print("Não encontrado chave. . .")


if __name__ == "__main__": 
    menu()