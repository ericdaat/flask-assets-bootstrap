from flask import Flask, render_template
from flask_assets import Bundle, Environment


# create app
app = Flask(__name__)

# assets: https://flask-assets.readthedocs.io/en/latest/
assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle(
    "assets/main.scss",
    filters="libsass",
    output="css/scss-generated.css"
)
assets.register("scss_all", scss)

# app routes
@app.route("/")
def index():
    return render_template("index.html")
