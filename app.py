### IMPORTS
from socket import gethostname

from flask import Flask, render_template, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flaskext.mysql import MySQL

from user import User
import graphs_api

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
    # On pythonanywhere
    app.config['MYSQL_DATABASE_USER'] = 'janoboril'
    app.config['MYSQL_DATABASE_DB'] = 'janoboril$MyWeb'
    app.config['MYSQL_DATABASE_HOST'] = 'janoboril.mysql.pythonanywhere-services.com'
mysql.init_app(app)

### SETUP LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"

@login_manager.user_loader
def load_user(user_id):
  return User.user_from_id(mysql, user_id)

### PAGE REQUEST HANDLERS
@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html", title=None)

@app.route("/pricing")
def pricing():
  return render_template("pricing.html", title=None)

@app.route("/login", methods=["GET","POST"])
def login():
  if not request.is_secure:
    print("Login over HTTP is not secure!!!! TODO: change this")
  
  if request.method == "POST":
    data = request.get_json()
    if "username" in data and "password" in data:
      user = User.verify_login(mysql, data["username"], data["password"])
      if user is None:
        return {"success": False, "message": "Incorrect username or password"}
      login_user(user)
      return  {"success": True, "message": ""}
    return {"success": False, "message": "The username or password were not posted"}

  return render_template("login.html", title=None)

@app.route("/logout")
def logout():
  logout_user()
  return {}

@app.route("/dashboard")
@login_required
def dashboard():
  return render_template("dashboard.html", title=None)

@app.route("/get-graphs")
@login_required
def get_graphs():
  userid = current_user.get_id()
  competitors = graphs_api.load_competitors(mysql, userid)
  graphs = graphs_api.fetch_graphs_from_api(*competitors)
  return  {"success": True, "graphs": graphs}

@app.route("/not-implemented")
def not_implemented():
  return "Not implemented"

if __name__ == "__main__":
  app.run()