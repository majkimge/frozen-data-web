### IMPORTS
from socket import gethostname

from flask import Flask, render_template, request
from flask_login import LoginManager, login_user, logout_user
from flaskext.mysql import MySQL;

from user import User

### INITIALIZE APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'TODO: CHANGE THIS SECRET KEY'

### INITALIZE DATABASE
mysql = MySQL()
if 'DESKTOP-VGO' in gethostname():
    # On local PC
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'frozen_data'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['MYSQL_DATABASE_PASSWORD'] = ""
else:
    # Elsewhere, when deployed
    raise Exception("No data given on how to connect to database")
mysql.init_app(app)

### SETUP LOGIN
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  with mysql.connect() as conn:
    with conn.cursor() as cursor:
      request, data = User.build_request(user_id)
      cursor.execute(request, data)
      data = cursor.fetchall()
  print(data)
  return User.get(data)

### PAGE REQUEST HANDLERS
@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html", title=None)

@app.route("/pricing")
def pricing():
  return render_template("pricing.html", title=None)

@app.route("/login")
def login():
  if not request.is_secure:
    print("Login over HTTP is not secure!!!! TODO: change this")
  
  #user = load_user(1)
  #login_user(user)
  logout_user()

  return render_template("login.html", title=None)

@app.route("/not-implemented")
def not_implemented():
  return "Not implemented"

if __name__ == "__main__":
  app.run()