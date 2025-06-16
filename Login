from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Cambia esto por una clave secreta segura

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = hash_password(request.form['password'])

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
            conn.commit()
            flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('El usuario ya existe.', 'danger')
            return redirect(url_for('register'))
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = hash_password(request.form['password'])

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password)).fetchone()
        conn.close()
        if user:
            session['user_id'] = user['id']
            session['email'] = user['email']
            flash('Bienvenido, has iniciado sesión.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'user_id' in session:
        return f"Hola, {session['email']}! <br><a href='/logout'>Cerrar sesión</a>"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
