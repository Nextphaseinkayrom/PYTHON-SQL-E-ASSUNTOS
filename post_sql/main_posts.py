print("1 - Arquive start")
import psycopg2

conexao = psycopg2.connect(dbname="meu_banco")
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS categorias")

cursor.execute("""
           CREATE TABLE IF NOT EXISTS categorias (
           id SERIAL PRIMARY KEY,
           nome TEXT
           )
           """)

cursor.executemany(
            "INSERT INTO categorias (nome) VALUES (%s)", 
            [("Alimentacao",), ("Lazer",), ("Transporte",) ]
        )


cursor.execute("SELECT * FROM categorias")
for cada in cursor.fetchall():
 id, nome = cada
 print(f"""       
       Id:  {id}
       Nome:{nome}""")


conexao.commit()
conexao.close()


#Exercicio de Post Simples