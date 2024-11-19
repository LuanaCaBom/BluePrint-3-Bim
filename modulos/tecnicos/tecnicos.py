from flask import Blueprint, render_template, request, redirect, flash
from models import Tecnicos
from database import db


bp_tecnico = Blueprint('tecnicos', __name__, template_folder="templates")


@bp_tecnico.route('/')
def index():
   dados = Tecnicos.query.all()
   return render_template('tecnico.html', tecnicos = dados)
  
@bp_tecnico.route('/add')
def add():
   return render_template('tecnico_add.html')


@bp_tecnico.route('/save', methods=['POST'])
def save():
   nome = request.form.get('nome')
   especialidade = request.form.get('especialidade')
   if nome and especialidade:
       bd_tecnico = Tecnicos(nome, especialidade)
       db.session.add(bd_tecnico)
       db.session.commit()
       flash('Técnico salvo com sucesso!!!')
       return redirect('/tecnicos')
   else:
       flash('Preencha todos os campos!!!')
       return redirect('/tecnicos/add')
  
@bp_tecnico.route('/remove/<int:id>')
def remove(id):
   dados = Tecnicos.query.get(id)
   if id > 0:
       db.session.delete(dados)
       db.session.commit()
       flash('Técnico removido com sucesso!!!')
       return redirect('/tecnicos')
   else:
       flash('Caminho incorreto!!!')
       return redirect('/tecnicos')


@bp_tecnico.route('/edita/<int:id>')
def edita(id):
   tecnicos = Tecnicos.query.get(id)
   return render_template('tecnico_edita.html', dados = tecnicos)


@bp_tecnico.route('/editasave', methods=['POST'])
def editasave():
   id = request.form.get('id')
   nome = request.form.get('nome')
   especialidade = request.form.get('especialidade')
   if id and nome and especialidade:
       tecnicos = Tecnicos.query.get(id)
       tecnicos.nome = nome
       tecnicos.especialidade = especialidade
       db.session.commit()
       flash('Dados atualizados com sucesso!!!')
       return redirect('/tecnicos')
   else:
       flash('Faltando dados!!!')
       return redirect('/tecnicos')


