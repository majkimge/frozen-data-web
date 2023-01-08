from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html", title=None, logged_in=None)

@app.route("/pricing")
def pricing():
  return render_template("pricing.html", title=None, logged_in=None)

@app.route("/not-implemented")
def not_implemented():
  return "Not implemented"

if __name__ == "__main__":
  app.run()