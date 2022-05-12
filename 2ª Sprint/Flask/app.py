from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('HOME.html')

@app.route('/vagas')
def pag_vagas():
    return render_template('VAGAS.html')

@app.route('/cursos')
def pag_cursos():
    return render_template('CURSOS.html')

@app.route('/métricas')
def pag_métricas():
    return render_template('MÉTRICAS.html')

@app.route('/localização')
def pag_localização():
    return render_template('LOCALIZAÇÃO.html')