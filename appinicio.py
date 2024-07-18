from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db_config = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin2024",
    database="ga_programmers"
)

cursor = db_config.cursor()

@app.route('/')
def index():
    cursor.execute('SELECT * FROM datos')
    tbusuarios = cursor.fetchall()
    return render_template('index.html', tbusuarios=tbusuarios)

@app.route('/iniciosesion', methods = ['GET', 'POST'])
def iniciosesion():
    if request.method == 'POST':
        email = request.form ['email']
        password = request.form ['password']
        cursor.execute('INSERT INTO tbusuarios (email, password) VALUES (%s, %s)', (email, password))
        db_config.commit()
        return redirect('/')
    return render_template('iniciosesion.html')

if __name__ == '__main__':
    app.run(debug=True)