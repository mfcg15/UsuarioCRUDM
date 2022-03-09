from flask import render_template, request, redirect
from flask_app.models.user import User
from flask_app import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/users")
def users():
    users = User.get_all()
    tamaño = len(users)
    return render_template('leer.html', all_friends = users, tamañoBase = tamaño)

@app.route("/users/new")
def usersNew():
    return render_template('crear.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route("/users/<int:id>")
def userID(id):
    idUsuario = id
    data = {
        "id": idUsuario,
    }
    usuario = User.get_user(data)
    return render_template('usuario.html', idusaurio = idUsuario, all_friends = usuario)

@app.route("/users/<int:id>/edit")
def userEditar(id):
    idUsuario = id
    data = {
        "id": idUsuario,
    }
    usuario = User.get_user(data)
    return render_template('editar.html', idusaurio = idUsuario, all_friends = usuario)

@app.route('/updated_user', methods=["POST"])
def userIDEditar():
    data = {
        "id": request.form["id"],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.update_user(data)
    iduser = request.form["id"]
    return redirect(f'/users/{iduser}')

@app.route("/<int:id>")
def RemoveID(id):
    idUsuario = id
    data = {
        "id": idUsuario,
    }
    User.delete_user(data)
    return redirect('/users')