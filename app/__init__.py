#       ?
import os

#       for make connections with DATABASE
import sqlalchemy

#       Microframework for smallest project
from flask import Flask,redirect

#       ?       
from yaml import load, Loader

#       for charge the environment variables
from dotenv import load_dotenv

#       ?
from os import environ

#       for the probleme of CORS
from flask_cors import CORS

#       create API object
from flask_restful import Api

#       create CONEXION object
from config import conexion

# Cargar todas las variables del archivo .env
load_dotenv()


#   def function for 
def init_connection_engine():
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            os.Error()
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

#   app object
app = Flask(__name__)

#   ?
api=Api(app)

#   CORS - Debug into the proper machine
CORS(app)

#   assign the parameter for other archive dont charge the github repo
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']

#   Set as false the modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#   init connection
conexion.init_app(app)

#   charge the secret key of developer
app.secret_key="secretKeyAndrew"

#   assign the values 
db = init_connection_engine()

#       async  , await

#   import the routes for 
from app import routes


#   

@app.route('/', methods=['GET','POST'])
def inicio():
    return redirect('/login')