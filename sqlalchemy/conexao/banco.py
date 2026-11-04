#
from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, DeclarativeBase

url = URL.create("postgresql+psycopg2", database="meu_banco")
engine = create_engine(url)

SessionLocal = sessionmaker(bind=engine)





#Descobrir como faz a conexao para o outro arquivo
#E fazer um sistema de criação simples (Parte c do Crud) 