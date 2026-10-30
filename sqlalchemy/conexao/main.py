from sqlalchemy import String, Integer, select
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

# nome = str(input("Digite o Nome: "))
# idade = int(input("Digite a Idade: "))
# usuario = Usuarios(nome=nome, idade=idade)
#sessao.add(usuario)
#sessao.commit()

 id = int(input("Digite o id da pessoa: "))
 with SessionLocal() as sessao:    
   print("Cadastro feito, mostrandos os resultados")
   usuarios = sessao.scalars(select(Usuarios).where(Usuarios.id == id)).first()
   if usuarios is None:
    print("Sem registro")
   else:
    print(f"Id: {usuarios.id} | Nome: {usuarios.nome} | Idade: {usuarios.idade}")
     
    # for inf in usuarios:
  #    print(f"Nome:{inf.nome} | Idade:{inf.idade}")
criar()





