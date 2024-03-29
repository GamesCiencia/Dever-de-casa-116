# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/Eu")
def home():

    nome = "Thomaz" # escreva seu nome
    idade = "13" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/Pai")
def home():

    nome = "José" # escreva seu nome
    idade = "60" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/Mãe")
def home():

    nome = "Ana" # escreva seu nome
    idade = "54" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo
@app.route("/Amigo")
def home():

    nome = "Lorenzo" # escreva seu nome
    idade = "14" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# adicione outras rotas, se você quiser
@app.route("/Amigo2")
def home():

    nome = "Enrico" # escreva seu nome
    idade = "13" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)



# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
