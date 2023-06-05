from flask import redirect,render_template, jsonify, request,session,abort
from app import app
from app import database as db_helper
# from google_auth_oauthlib.flow import Flow
import pathlib
import os
# from google.oauth2 import id_token
# import google.auth.transport.requests
from pip._vendor import cachecontrol
import requests

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"



# GOOGLE_CLIENT_ID="684001424694-ulpvpg58u0npqat2oqb9lka4dsjlp8ad.apps.googleusercontent.com"
# client_secrets_file=os.path.join(pathlib.Path(__file__).parent,"client_secret.json")

#flow=Flow.from_client_secrets_file(
#    client_secrets_file=client_secrets_file,
#    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
#    redirect_uri="http://127.0.0.1:5000/callback"
#    )

#  RC
'''
#@app.route("/", methods=['GET'])
#def front():
#    return render_template ('frontPage.html')

#@app.route("/formOFcv", methods=['GET','POST'])
#def formcvPage():
#    return render_template ('auth/register.html')

#@app.route("/base", methods=['GET','POST'])
#def testBase():
#    return render_template ('base.html')

#@app.route("/loginT", methods=['GET','POST'])
#def loginT():
#    return render_template ('auth/login.html')
    # return redirect ("/protected_area")
    
#@app.route("/login", methods=['GET','POST'])
#def login():
    # session["google_id"]="Test"
    # # return render_template ('auth/login.html')
    # return redirect ("/protected_area")
#    authorization_url, state = flow.authorization_url()
#    session["state"] = state
#    return redirect(authorization_url)

@app.route("/register", methods=['GET','POST'])
def formToCV():
    return render_template ('auth/register.html')

@app.route("/cvexample", methods=['POST'])
def cvclone():
    return render_template ('cvClone.html')

@app.route("/returncv", methods=['GET','POST'])
def formofcv():
    return render_template ('cvOfForm.html')

@app.route("/test01", methods=['GET','POST'])
def test():
    return render_template ('testHTML.html')


@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)
'''
@app.route("/todoList", methods=['POST','GET'])
def pageTodoList():
    items = db_helper.fetch_todo()
    return render_template("todoList.html", items=items)

'''
@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    data = request.get_json()
    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

'''
# For Google Authetication


'''

def login_is_required(function):
    def wrapper(*args,**kwargs):
        if "google_id" not in session:
            abort(401)
        else:
            return function()
    return wrapper

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")

@app.route("/logout")
def logout():
    print("Ingreso al session.clear()")
    session.clear()
    return redirect ("/ll")


@app.route("/ll")
def ll():
    return "Go to Login Page <a href='/login'><button>Go Login</button></a>"

@app.route("/protected_area")
@login_is_required
def protected_area():
    return "Go to Login Page <a href='/logout'><button>Go Logout</button></a>"
    return "Welcome to Protected Page"



@app.route("/testJS",methods=['POST','GET'])
def testJS():
    nombre=request.form.get("nameF")
    apellido=request.form.get("apellidoF")
    telefono=request.form.get("telefonoF")
    gmail=request.form.get("correoF")
    nivelEnglish=request.form.get("nivelEnglishF")
    habilidades=[request.form.get("habilidadesF1"),request.form.get("habilidadesF2"),request.form.get("habilidadesF3"),request.form.get("habilidadesF4")]
    aptitudes=[request.form.get("aptitudesF1"),request.form.get("aptitudesF2"),request.form.get("aptitudesF3"),request.form.get("aptitudesF3"),request.form.get("aptitudesF5")]
    return render_template ("cv/cv01.html",nombre=nombre,apellido=apellido,telefono=telefono,gmail=gmail,nivelEnglish=nivelEnglish,habilidades=habilidades,aptitudes=aptitudes,experiancia=experiancia)

'''