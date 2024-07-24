from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # appel des configuration du dossier config.py
from app import routes
