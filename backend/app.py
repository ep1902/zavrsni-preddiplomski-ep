from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hejj"
    #return render_template("index.html")
