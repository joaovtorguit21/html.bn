from flask import Flask ,render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")




@app.route("/loginclinte")
def clintelog():
    return render_template("LOGINCLINTE.html")
























if __name__ in "__main__":
  app.run (debug=True)