from flask import *
import json
import priems
app = Flask(__name__)

f = open("zadacha.json", "r", encoding="utf-8")
dict = json.load(f)

#делает основную страницу
@app.route("/", methods=["POST", "GET"])
def index():
    # if request.method == "POST":
    #     print(list(request.form.values()))
    return render_template("index.html", priems = list(enumerate(priems.down_list())))

#делает страницу с ответами
@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        better = int(request.form.getlist("better")[0])
        worse = int(request.form.getlist("worse")[0])
        results = priems.answer(better, worse)
        return render_template("answer.html", question = results, system = dict["system"], features = list(enumerate(dict["features"])), scenarei = list(enumerate(dict["scenarei"])), task = dict["task"], roles = list(enumerate(dict["roles"].keys())))

# @app.route("/result", methods=["POST"])
# def result():
#     return render_template("index.html", priems = list(enumerate(priems.down_list())))

app.run()