from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db_config = {
    'Host':'localhost',
    'user': 'admin',
    'password':'admin2024'
}