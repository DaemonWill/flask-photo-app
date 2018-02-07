from flask import Flask
from werkzeug.utils import secure_filename
app = Flask(__name__)
from app import views
