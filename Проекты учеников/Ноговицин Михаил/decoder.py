import json
from colorama import Fore, Style
import random
from gensim.models import KeyedVectors
from ufal.udpipe import Model, Pipeline


def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL):
    print(f"{brightness}{color}{s}{Style.RESET_ALL}")


model = KeyedVectors.load_word2vec_format("model.bin", binary=True)
mod = Model.load('udpipe_syntagrus.model')
pipeline = Pipeline(mod, 'tokenize', Pipeline.DEFAULT, Pipeline.DEFAULT, 'conllu')


def no_parsing(sv):
    if sv.lower().startswith("не"):
        sv = sv[2:]
    elif sv.lower().startswith("без"):
        sv = sv[3:]
    else:
        sv = "не" + sv

    w = "".join(process(sv))

    if w in model:
        return [i for i in model.most_similar(positive=[w], topn=50) if i[0].split("_")[1] == "ADJ"][0][0].split("_")[0]

    return sv


def process(text='Строка'):
    processed = pipeline.process(text)
    content = [l for l in processed.split('\n') if not l.startswith('#')]

    tagged = [w.split('\t') for w in content if w]

    for t in tagged:
        (word_id, token, lemma, pos, xpos, feats, head, deprel, deps, misc) = t
        if not lemma or not token:
            continue
        tagged_propn = '%s_%s' % (lemma, pos)

    return tagged_propn


f = open("task.json", "r", encoding="utf-8")

dictionary = json.load(f)

for sv in dictionary["features"]:
    print(f"Изменить свойство {dictionary['system']} на {no_parsing(sv)}")
    system = process(dictionary["system"])
    sv = process(sv)
    if system in model and sv in model:
        w = [i[0].split("_")[0] for i in  model.most_similar(positive=[system], negative=[sv], topn=50) if i[0].split("_")[1]=="NOUN"][0]
        print(f"Пожойдет ли вам вместо {system} {w}")



for role in dictionary["roles"]:
    for isp in dictionary["roles"][role]:
        for sv in dictionary["roles"][role][isp]:
            i = process(isp)
            s = process(sv)
            if s in model and i in model:
                w = model.most_similar(positive=[i], negative=[s], topn=1)[0][0]
                print(f"Подойдет ли вам вместо {isp}  {w.split('_')[0]}")
            print(f"Изменить свойство {isp} на {no_parsing(sv)}")
