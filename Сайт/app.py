from flask import *
import pymorphy3
import re
import final_backend
import priems
app = Flask(__name__)

m_analyzer = pymorphy3.MorphAnalyzer()


dictionary = {}

@app.route('/')
def index():
    dictionary[request.remote_addr] = {}
    return render_template("index.html", priems = list(enumerate(priems.down_list())))

@app.route("/answer", methods=["POST"])
def answer():
    for e in request.form.values():
        for w in e:
            if w in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
                isps = []
                for role in dictionary[request.remote_addr]["roles"].keys():
                    isps += list(dictionary[request.remote_addr]["roles"][role])
                return render_template("submit-end.html", isps =isps , system = dictionary[request.remote_addr]["system"],
                                       error = "Английские символы запрещены!",
                                       scroll_to='#scrollspyHeading3')

    dictionary[request.remote_addr]["features"] = request.form["system_feat"].split(", ")
    for role in dictionary[request.remote_addr]["roles"]:
        for isp in dictionary[request.remote_addr]["roles"][role]:
            dictionary[request.remote_addr]["roles"][role][isp] = request.form[isp].lower().split(", ")
    dictionary[request.remote_addr].pop("system_candidates")
    dictionary[request.remote_addr].pop("roles_cand")
    results = final_backend.dict_to_list(dictionary[request.remote_addr])
    results = list(enumerate(results + priems.answer(dictionary[request.remote_addr]["better"], dictionary[request.remote_addr]["worse"])))
    return render_template("answer.html", question=results, system = dictionary[request.remote_addr]["system"],
                           features = list(enumerate(dictionary[request.remote_addr]["features"])),
                           scenarei = list(enumerate(dictionary[request.remote_addr]["scenario"])),
                           task = dictionary[request.remote_addr]["task"],
                           roles = list(enumerate(dictionary[request.remote_addr]["roles"].keys())),
                                       scroll_to='#scrollspyHeading3')


@app.route("/submit", methods = ["POST"])
def submit():
    for e in request.form.values():
        for w in e:
            if w in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
                return render_template("index.html",  priems = list(enumerate(priems.down_list())), error = "Английские символы запрещены!",
                                       scroll_to='#scrollspyHeading3')

    better = int(request.form.getlist("better")[0])
    worse = int(request.form.getlist("worse")[0])
    dictionary[request.remote_addr]["better"] = better
    dictionary[request.remote_addr]["worse"] = worse
    task = request.form["task"].lower()
    description = request.form["description"].lower()
    aims = request.form["aims"].lower().split(", ")
    scenarium = request.form["scenarium"].lower().split(", ")
    roles = request.form["roles"].lower().split(", ")

    roles = [r for r in roles if r.replace(" ","") != ""]
    scenarium = [r for r in scenarium if r.replace(" ","") != ""]
    aims = [r for r in aims if r.replace(" ", "") != ""]

    string = re.sub(r"\W", " ", description+" "+task).split()
    spisok = []
    for word in set(string):
        former = m_analyzer.parse(word)[0]
        if 'NOUN' == former.tag.POS:
            spisok.append(former.normal_form)
    dictionary[request.remote_addr]["system_candidates"] = spisok
    dictionary[request.remote_addr]["roles_cand"] = roles
    dictionary[request.remote_addr]["scenario"] = scenarium
    dictionary[request.remote_addr]["aims"] = aims
    dictionary[request.remote_addr]["task"] = task
    dictionary[request.remote_addr]["description"] = description

    return render_template("submit.html", spisok=spisok, roles =roles,
                                   scroll_to='#scrollspyHeading3')

@app.route("/submit2", methods = ["POST"])
def submit2():
    isps = []
    for e in request.form.values():
        for w in e:
            if w in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
                return render_template("submit.html",  spisok=dictionary[request.remote_addr]["system_candidates"],
                                       roles = dictionary[request.remote_addr]["roles_cand"],
                                       error = "Английские символы запрещены!",
                                       scroll_to='#scrollspyHeading3')

    dictionary[request.remote_addr]["system"] = request.form.getlist("system_end")[0]
    dictionary[request.remote_addr]["roles"] = {}


    for role in dictionary[request.remote_addr]["roles_cand"]:
        if not request.form.get(role)  is None and request.form[role].replace(" ","") != "":
            dictionary[request.remote_addr]["roles"][role] = {i:None for i in request.form[role].lower().split(", ")}
            isps += request.form[role].lower().split(", ")

    return render_template("submit-end.html", isps = isps, system = dictionary[request.remote_addr]["system"],
                                       scroll_to='#scrollspyHeading3')


app.run()