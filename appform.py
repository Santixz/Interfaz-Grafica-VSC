from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',       # Host donde está alojada la base de datos
    'user': 'admin',      # Nombre de usuario de MySQL
    'password': 'admin2024', # Contraseña de MySQL
    'database': 'ga_programmers'   # Nombre de la base de datos
}


def insertar_usuario(nombre, apellido, email, contrasena):
    try: 

        conn = mysql.connector.connect(**db_config)


        cursor= conn.cursor()


        cursor.execute('INSERT INTO tbusers (nombre, apellido, email, contrasena) VALUES (%s, %s, %s, %s)', (nombre, apellido, email, contrasena))


        conn.commit()


    except mysql.connector.Error as err:

        print(f"Error: {err}")


        flash('Error al insertar el usuario.')


    finally:

        conn.close()

    
def obtener_usuarios():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute ('SELECT idusers, nombre, apellido, email FROM tbusers')
        users = cursor.fetchall()
        return users
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash('Error al obtener los usuarios.')
        return []
    finally:
        conn.close()

@app.route('/')
def Registrarse ():
    return render_template('registrarse.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    contrasena = request.form['contrasena']

    if not nombre or not apellido or not email or not contrasena:
        flash('Todos los campos son obligatorios.')
        return redirect(url_for('registrarse'))
    
    insertar_usuario(nombre, apellido, email, contrasena)

    return redirect(url_for('exito'))

@app.route('/usuarios')
def mostrar_usuarios():
    users = obtener_usuarios()
    return render_template('users.html', users=users)

@app.route ('/eliminar_usuario/<int:id>' , methods= ['POST'])
def eliminar_usuario(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute ('DELETE FROM tbusers WHERE id = %s' , (id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error al eliminar el usuario. {err}")
        flash('Error al eliminar el usuario.')
    finally:
        conn.close()
    return redirect(url_for('mostrar_usuarios'))

@app.route('/actualizar_usuario/<int:id>' , methods=['GET'])
def mostrar_Registrarse_actualizar_usuario(id):
    try:
        conn = mysql.connector.connect (**db_config)
        cursor = conn.cursor()
        cursor.execute ('SELECT idusers, nombre, email, contrasena FROM tbusers WHERE id = %s' , (id,))
        usuario = cursor.fetchone ()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash('Error al actualizar el usuario.')
        usuario = None
    finally:
        conn.close()
    if usuario:
        return render_template('actualizar_usuarios.html' , id=id, nombre=usuario[0], email=usuario[1])
    else:
        return redirect(url_for('mostrar_usuarios'))
    
@app.route('/actualizar_usuario/<int:id>' , methods = ['POST'])
def actualizar_usuario(id):
    nuevo_nombre = request.form ['nuevo_nombre']
    nuevo_email = request.form ['nuevo_email']
    nueva_contrasena = request.form ['nueva_contrasena']

    if not nuevo_nombre or not nuevo_email or not nueva_contrasena:
        flash ('Todos los campos son obligatorios.')
        return redirect(url_for('mostrar_Registrarse_actualizar_usuarios' , id=id))
    
    try:
        conn = mysql.connector.connect (**db_config)
        cursor = conn.cursor()
        cursor.execute ('UPDATE tbusers SET nombre = %s, email = %s, contrasena = %s WHERE id = %s' , (nuevo_nombre, nuevo_email, nueva_contrasena, id))
        conn.commit()
    except mysql.connector.Error as err:
        print (f"Error: {err}")
        flash ('Error al actualizar el usuario.')
    finally:
        conn.close()
    return redirect(url_for('mostrar_usuarios'))

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__ == '__main__':
    app.run(debug=True)