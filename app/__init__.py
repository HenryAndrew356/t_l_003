import os
import sqlalchemy
from flask import Flask,redirect
from yaml import load, Loader
from dotenv import load_dotenv
from os import environ
from flask_cors import CORS
from flask_restful import Api
from config import conexion

# Cargar todas las variables del archivo .env
load_dotenv()

def init_connection_engine():
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            OSError()
        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST')
        )
    )
    return pool
app = Flask(__name__)
api=Api(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
conexion.init_app(app)
app.secret_key="secretKeyAndrew"
db = init_connection_engine()
from app import routes

@app.route('/', methods=['GET','POST'])
def inicio():
    return redirect('/login')