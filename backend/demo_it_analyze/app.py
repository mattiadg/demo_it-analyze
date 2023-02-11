from flask import Flask, request, render_template

from demo_it_analyze.nlp.ner import compute_ner

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("analysis.html")


@app.route("/ner", methods=["POST"])
def ner():
    text = request.data.decode()
    entities = compute_ner(text)
    return [ent.json() for ent in entities]
