from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'STRINgqUENINGUémsAbe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/BluePrint"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLACHEMY_TRACK_MODIFICATIOS'] = False
from database import db
from flask_migrate import Migrate
from models import Tecnicos, Projetos
db.init_app(app)
migrate = Migrate(app, db)
from modulos.tecnicos.tecnicos import bp_tecnico
app.register_blueprint(bp_tecnico, url_prefix='/tecnicos')
from modulos.projetos.projetos import bp_projeto
app.register_blueprint(bp_projeto, url_prefix='/projetos')

@app.route('/')
def index():
    return render_template("ola.html")
