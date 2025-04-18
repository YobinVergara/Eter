from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

# Iniciar la app de Flask
app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient("mongodb+srv://yobinvergara:1006037426yobin@cluster0.hgxyeef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['eter']
collection = db['usuarios']

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para registrar un nuevo usuario
@app.route('/registrar.html', methods=['POST'])
def registrar():
    usuario = request.form['usuario']
    clave = request.form['clave']
    
    # Crear un nuevo usuario en la base de datos
    new_user = {
        'usuario': usuario,
        'clave': clave
    }
    
    collection.insert_one(new_user)
    
    return redirect(url_for('index'))

# Ruta para login (validar usuario)
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    clave = request.form['clave']
    
    user = collection.find_one({'usuario': usuario})
    
    if user and user['clave'] == clave:
        return "Inicio de sesión exitoso"
    else:
        return "Usuario o contraseña incorrectos"

if __name__ == '__main__':
    app.run(debug=True)
