import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="andrew",
    password="sys.admin@password123",
    database="Alunos",
    port="3306"
)

ALUNO_CADASTRADO_COM_SUCESSO = 0
FALHA_NO_CADASTRO = 1

ALUNO_REMOVIDO_COM_SUCESSO = 0
FALHA_NA_REMOCAO = 1

cursor = bd.cursor()

def pegar_alunos():
    cursor.execute("select nome, matricula from alunos")
    return cursor.fetchall()

def pegar_aluno_por_nome(nome):
    cursor.execute(f"SELECT nome, matricula FROM alunos WHERE nome LIKE \"{nome.strip()}\"")
    return cursor.fetchall()

def pegar_aluno_por_matricula(matricula):
    cursor.execute(f"SELECT nome, matricula, senha FROM alunos WHERE matricula=\"{matricula.strip()}\"")
    return cursor.fetchall()

def cadastrar_aluno(nome, matricula, senha):
    alunos = pegar_alunos()
    if nome != "" and matricula!= "":
        if not (nome, matricula) in alunos:
            try:
                cursor.execute(
                    f"""
                    insert into alunos VALUES
                    (\"{nome}\", \"{matricula}\",\"{senha}\");
                    """
                )
            except:
                return FALHA_NO_CADASTRO
            return ALUNO_CADASTRADO_COM_SUCESSO
    return FALHA_NO_CADASTRO

def remover_aluno(nome, matricula):
    try:
        cursor.execute(f"DELETE FROM `alunos` WHERE nome=\"{nome}\" AND matricula=\"{matricula}\"")
        return ALUNO_REMOVIDO_COM_SUCESSO
    except:
        return FALHA_NA_REMOCAO


def finalizar_conexao():
    bd.close()

if __name__ == "__main__":
    print(bd.is_connected())
    print(pegar_aluno_por_nome("andrew"))
    print(cadastrar_aluno("Dylan", "20201TIINF0028", '123'))
    print(pegar_alunos())
    #print(remover_aluno('Dylan','20201TIINF0028'))
    print(pegar_alunos())
    print(pegar_aluno_por_matricula("20191TIINF0028"))
    finalizar_conexao()