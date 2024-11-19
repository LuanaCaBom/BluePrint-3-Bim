from flask import Blueprint, render_template, request, redirect, flash
from models import Projetos, Tecnicos
from database import db

bp_projeto = Blueprint('projetos', __name__, template_folder="templates")

@bp_projeto.route('/')
def index():
    dados = Projetos.query.all()
    return render_template('projeto.html', projetos = dados)
    
@bp_projeto.route('/add')
def add():
    t = Tecnicos.query.all()
    return render_template('projeto_add.html', tecnicos = t)

@bp_projeto.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    ano_inicio = request.form.get('ano_inicio')
    id_tecnico = request.form.get('id_tecnico')
    if nome and ano_inicio and id_tecnico:
        bd_projeto = Projetos(nome, ano_inicio, id_tecnico)
        db.session.add(bd_projeto)
        db.session.commit()
        flash('Projeto salvo com sucesso!!!')
        return redirect('/projetos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/projetos/add')
    
@bp_projeto.route('/remove/<int:id>')
def remove(id):
    dados = Projetos.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Projeto removido com sucesso!!!')
        return redirect('/projetos')
    else:
        flash('Caminho incorreto!!!')
        return redirect('/projetos')

@bp_projeto.route('/edita/<int:id>')
def edita(id):
    projetos = Projetos.query.get(id)
    tecnicos = Tecnicos.query.all()
    return render_template('projeto_edita.html', dados = projetos, tecnicos = tecnicos)

@bp_projeto.route('/editasave', methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    ano_inicio = request.form.get('ano_inicio')
    id_tecnico = request.form.get('id_tecnico')
    if id and nome and ano_inicio and id_tecnico:
        projetos = Projetos.query.get(id)
        projetos.nome = nome
        projetos.ano_inicio = ano_inicio
        projetos.id_tecnico = id_tecnico
        db.session.commit()
        flash('Dados atualizados com sucesso!!!')
        return redirect('/projetos')
    else: 
        flash('Faltando dados!!!')
        return redirect('/projetos')
