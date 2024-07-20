from flask import *
import pymorphy3
import re
app = Flask(__name__)

m_analyzer = pymorphy3.MorphAnalyzer()

dictionary = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/answer", methods=["POST"])
def answer():
    for role in dictionary["roles"]:
        for isp in dictionary["roles"][role]:
            dictionary["roles"][role][isp] =  request.form[isp].lower().split(", ")
    dictionary.pop("system_candidates")
    dictionary.pop("roles_cand")
    print(dictionary)
    return render_template("answer.html")

@app.route("/submit", methods = ["POST"])
def submit():
    if request.method == "POST":
        task = request.form["task"]
        description = request.form["description"]
        aims = request.form["aims"].split(", ")
        scenarium = request.form["scenarium"].split(", ")
        roles = request.form["roles"].split(", ")
        string = re.sub(r"\W", " ", description+" "+task).split()
        spisok = []
        for word in set(string):
            former = m_analyzer.parse(word)[0]
            if 'NOUN' == former.tag.POS:
                spisok.append(former.normal_form)
        dictionary["system_candidates"] = spisok
        dictionary["roles_cand"] = roles
        dictionary["scenario"] = scenarium
        dictionary["aims"] = aims
        dictionary["task"] = task
        dictionary["description"] = description
        dictionary["features"] = request.form["system_feat"]
        return render_template("homes.html", spisok=spisok, roles =roles)
    return render_template("index.html")

@app.route("/submit2", methods = ["POST"])
def submit2():
    for sys in dictionary["system_candidates"]:
        if request.form[sys].lower().startswith("да"):
            dictionary["system"] = sys
            break
    dictionary["roles"] = {}
    isps = []
    for role in dictionary["roles_cand"]:
        dictionary["roles"][role] = {i:None for i in request.form[role].lower().split(", ")}
        isps += request.form[role].lower().split(", ")

    return render_template("submit-end.html", isps = isps)


app.run()