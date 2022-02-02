from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import sql

app = Flask("App")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        matricula = request.form["txt_login"]
        senha = request.form["senha_login"]
        aluno = sql.pegar_aluno_por_matricula(matricula)

        if len(aluno) == 0 or aluno[0][2] != senha:
            return redirect(url_for("login_falha"))

        return redirect(url_for("usuario", matricula=matricula))

@app.route('/login/falha', methods=["GET", "POST"])
def login_falha():
    if request.method == "GET":
        return render_template('login_falha.html')
    else:
        matricula = request.form["txt_login"]
        senha = request.form["senha_login"]
        aluno = sql.pegar_aluno_por_matricula(matricula)

        if len(aluno) == 0 or aluno[0][2] != senha:
            return redirect(url_for("login_falha"))

        return redirect(url_for("usuario", matricula=matricula))

@app.route('/cadastro',methods=["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template('cadastro.html', msgErro="")
    else:
        matricula = request.form["txtMatricula"]
        nome = request.form["txtNome"]
        senha = request.form["txtSenha"]
        senha2 = request.form["txtSenha2"]

        if matricula == "" or nome == "" or senha == "" or senha2 == "":
           return render_template('cadastro.html', msgErro='Preencha todos os campos')  
        elif senha != senha2:
           return render_template('cadastro.html', msgErro='As senhas não são iguais')

        foi_cadastrado = sql.cadastrar_aluno(nome, matricula, senha)

        if foi_cadastrado == sql.FALHA_NO_CADASTRO:
            if matricula == sql.pegar_aluno_por_matricula(matricula)[0][1]:
                return render_template('cadastro.html', msgErro='Úsuario já cadastrado')
        
        return redirect(url_for('login'))


@app.route('/login/<matricula>')
def usuario(matricula):
    return render_template('Usuarios.html')

if __name__ == "__main__":
    app.run(debug=True)
    sql.finalizar_conexao()