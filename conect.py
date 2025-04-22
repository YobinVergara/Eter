from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

print("Activo")

app = Flask(__name__)

# Conectar a MongoDB Atlas
client = MongoClient("mongodb+srv://yobinvergara:1006037426yobin@cluster0.hgxyeef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['eter']
usuarios = db['usuarios']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario_input = request.form['usuario']
    clave_input = request.form['clave']

    print("Usuario ingresado:", usuario_input)
    print("Contraseña ingresada:", clave_input)

    # Verificamos si el usuario existe
    usuario_encontrado = usuarios.find_one({
        "$or": [
            {"usuario": usuario_input},
            {"correo": usuario_input}
        ],
        "clave": clave_input
    })

    if usuario_encontrado:
        print("✅ Usuario autenticado correctamente.")
        return redirect(url_for('home'))  # O redirige donde quieras
    else:
        print("❌ Usuario o contraseña incorrectos.")
        return "Usuario o contraseña incorrectos", 401

if __name__ == '__main__':
    app.run(debug=True)
