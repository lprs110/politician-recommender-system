from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, login_manager

from app.models.tables import User, Area, Candidate
from app.models.forms import LoginForm, RegisterForm


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Login feito com sucesso")
            return redirect(url_for('index'))
        else:
            flash("Login inválido")

    return render_template('login.html', form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data, form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Cadastrado realizado com sucesso")
        return redirect(url_for('index'))

    return render_template('register.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Usuário deslogado")
    return redirect(url_for('index'))

'''
@app.route("/create_area")
def create_area():
    areas = ["cultura", "economia", "educacao", "meio_ambiente", "saude", "seguranca", "tecnologia"]

    for area in areas:
        a = Area(area)
        db.session.add(a)
    db.session.commit()

    return "Ok"


@app.route("/create_candidate")
def create_candidate():
    candidates = ['alckmin', 'amoedo', 'bolsonaro', 'ciro', 'daciolo', 'boulos', 'haddad', 'marina']

    for candidate in candidates:
        c = Candidate(candidate)
        db.session.add(c)
    db.session.commit()

    return "Okkkk"
'''
