from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route('/detalhecurso')
def detalhecurso():
    return render_template("detalhecurso.html")

@app.route('/disciplina')
def disciplina():
    return render_template("disciplina.html")

@app.route('/listacursos')
def listacursos():
    return render_template("listacursos.html")

@app.route('/noticias')
def noticias():
    return render_template("noticias.html")

app.run()