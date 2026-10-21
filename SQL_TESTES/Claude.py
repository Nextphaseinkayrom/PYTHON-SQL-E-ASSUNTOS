import sqlite3

BANCO = "banco.db"


# ---------- Banco ----------

def conectar():
    conexao = sqlite3.connect(BANCO)
    conexao.execute(
        """CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            idade INTEGER NOT NULL
        )"""
    )
    conexao.commit()
    return conexao


def buscar_por_id(conexao, id_pessoa):
    return conexao.execute(
        "SELECT id, nome, idade FROM pessoas WHERE id = ?",
        (id_pessoa,),
    ).fetchone()


# ---------- Entrada segura ----------

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números inteiros.")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Não pode ficar vazio.")


# ---------- Operações do CRUD ----------

def registrar(conexao):
    print("\nCREATE")
    nome = ler_texto("Nome: ")
    idade = ler_inteiro("Idade: ")
    try:
        conexao.execute(
            "INSERT INTO pessoas (nome, idade) VALUES (?, ?)",
            (nome, idade),
        )
        conexao.commit()
        print("Pessoa registrada.")
    except sqlite3.IntegrityError:
        print("Já existe uma pessoa com esse nome.")


def exibir(conexao):
    print("\nREAD ALL")
    pessoas = conexao.execute(
        "SELECT id, nome, idade FROM pessoas"
    ).fetchall()

    if not pessoas:
        print("Não encontramos nenhum usuário no momento.")
        return

    for id_, nome, idade in pessoas:
        print(f"ID: {id_} | Nome: {nome} | Idade: {idade}")


def localizar(conexao):
    print("\nFOUNDER")
    pessoa = buscar_por_id(conexao, ler_inteiro("Digite o ID: "))

    if pessoa is None:
        print("Não encontramos.")
        return

    _, nome, idade = pessoa
    print(f"Encontramos: {nome}, {idade} anos.")


def modificar(conexao):
    print("\nUPDATE")
    pessoa = buscar_por_id(conexao, ler_inteiro("ID exato da pessoa: "))

    if pessoa is None:
        print("Não encontramos.")
        return

    id_, nome, idade = pessoa
    print(f"Atual -> Nome: {nome} | Idade: {idade}")
    campo = ler_inteiro("Modificar: 1 = Nome / 2 = Idade: ")

    if campo == 1:
        sql = "UPDATE pessoas SET nome = ? WHERE id = ?"
        novo = ler_texto("Novo nome: ")
    elif campo == 2:
        sql = "UPDATE pessoas SET idade = ? WHERE id = ?"
        novo = ler_inteiro("Nova idade: ")
    else:
        print("Opção inválida.")
        return

    try:
        conexao.execute(sql, (novo, id_))
        conexao.commit()
        print("Atualizado.")
    except sqlite3.IntegrityError:
        print("Já existe uma pessoa com esse nome.")


def deletar(conexao):
    print("\nDELETE")
    pessoa = buscar_por_id(conexao, ler_inteiro("ID da pessoa: "))

    if pessoa is None:
        print("Não encontramos.")
        return

    id_, nome, idade = pessoa
    print(f"Informações -> ID: {id_} | Nome: {nome} | Idade: {idade}")

    if ler_inteiro("Deseja apagar mesmo? 1 = Sim / 2 = Não: ") == 1:
        conexao.execute("DELETE FROM pessoas WHERE id = ?", (id_,))
        conexao.commit()
        print("Pessoa removida.")
    else:
        print("Operação cancelada.")


# ---------- Menu ----------

OPCOES = {
    1: ("Registro", registrar),
    2: ("Exibição de users", exibir),
    3: ("Localizador de IDs", localizar),
    4: ("Modificador", modificar),
    5: ("Deletador", deletar),
}


def main():
    conexao = conectar()
    try:
        while True:
            print("\n--- MENU ---")
            for numero, (titulo, _) in OPCOES.items():
                print(f"{numero} -- {titulo}")
            print("0 -- Sair")

            escolha = ler_inteiro("Sua resposta: ")

            if escolha == 0:
                break
            if escolha in OPCOES:
                _, funcao = OPCOES[escolha]
                funcao(conexao)
            else:
                print("Opção inválida.")
    finally:
        conexao.close()


if __name__ == "__main__":
    main()

#Criado pelo Claude