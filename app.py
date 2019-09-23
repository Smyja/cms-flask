from flask import Flask, render_template, abort, Response
from buttercms.blog_blueprint import blog


app = Flask(__name__)

app.register_blueprint(blog, url_prefix='/blog')


@app.route("/")
def homepage():
   return render_template ("index.html")

@app.route("/portfolio")
def portfolio():
   return render_template ("portfolio.html")