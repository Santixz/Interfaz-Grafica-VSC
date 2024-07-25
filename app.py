from flask import Flask, render_template, request, redirect, seccion, url_for
import mysql.connector
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'