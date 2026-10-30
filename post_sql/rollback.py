# O exercicio é básicamente errar e explicar o motivo do erro
#É igual o Raise do Python normal e do Except
#E também tem ensinamento de conexao do PostgreSql

from psycopg2 import errors
import psycopg2

conexao = psycopg2.connect(dbname="meu_banco")
cursor = conexao.cursor()


#cursor.execute("DROP TABLE IF EXISTS categoria")

cursor.execute("""
            CREATE TABLE categoria (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL UNIQUE
            )
            """)

print("Conectado.")
try:
    cursor.execute("INSERT INTO categoria(nome) VALUES (%s)", ("Lazer",))
    conexao.commit()
except errors.UniqueViolation:
    conexao.rollback()
    print("Essa categoria já existe")
