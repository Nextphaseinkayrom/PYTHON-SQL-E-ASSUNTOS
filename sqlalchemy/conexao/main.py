from sqlalchemy import String, Integer, select, update, delete
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


from banco import engine, SessionLocal

def criar():
 class Base(DeclarativeBase):
    pass
 
 class Usuarios(Base):
    __tablename__ = "tabela"

    id: Mapped[int] = mapped_column(Integer, nullable=True, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=True)
    idade: Mapped[int] = mapped_column(Integer, nullable=True)
 Base.metadata.create_all(engine)

#Criação de nome e idade do usuario (CREATE)
# nome = str(input("Digite o Nome: "))
# idade = int(input("Digite a Idade: "))
# usuario = Usuarios(nome=nome, idade=idade)
#sessao.add(usuario)
#sessao.commit()

#Read Feito.
 print("PASSO 1 - Localização de ID 1/3 (READ)")
 id = int(input("Digite o id da pessoa: "))
 with SessionLocal() as sessao:
   usuarios = sessao.scalars(select(Usuarios).where(Usuarios.id == id)).first()
   if usuarios is None:
    print("Sem registro")
   else:
    print(f"Id: {usuarios.id} | Nome: {usuarios.nome} | Idade: {usuarios.idade}")
    
#Update feito.    
   # print("PASSO 2 MODIFICAÇÃO DE NOME/IDADE 2/3 (UPDATE)")
   # mod = int(input("Digite 1/2"))
   # if mod == 1:
    #nome_mod = str(input("Digite o nome de mudança: "))
     #sessao.execute(
     #  update(Usuarios).where(Usuarios.id == id).values(nome=nome_mod))
     #sessao.commit() 
     #print(f"Nome atualizado!\n Novo nome {usuarios.nome}")
#
#Delete Pendente.
    
    deg = int(input("Digite um id para ser Excluido"))
    if deg:
      resultado = sessao.execute(
        delete(Usuarios).where(Usuarios.id == deg)
      )
      sessao.commit()

      if resultado.rowcount > 0:
        print("Usuario deletado.")
      else:
        print("Não encontrado")

criar()





