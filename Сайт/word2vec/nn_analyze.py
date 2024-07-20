
from gensim.models import KeyedVectors
from ufal.udpipe import Model, Pipeline

print("Loading...")
model = KeyedVectors.load_word2vec_format("word2vec/model.bin", binary=True)
mod = Model.load('word2vec/udpipe_syntagrus.model')
pipeline = Pipeline(mod, 'tokenize', Pipeline.DEFAULT, Pipeline.DEFAULT, 'conllu')
print("Completed")
def process(text='Строка'):
    processed = pipeline.process(text)
    content = [l for l in processed.split('\n') if not l.startswith('#')]

    tagged = [w.split('\t') for w in content if w]
    tagged_propn = ""
    for t in tagged:
        (word_id, token, lemma, pos, xpos, feats, head, deprel, deps, misc) = t
        if not lemma or not token:
            continue
        tagged_propn = '%s_%s' % (lemma, pos)

    return tagged_propn


def parsing(sv, system):
    system = process(system)

    sv = process(sv)
    if system in model and sv in model:
        sv_new =  [i[0].split("_")[0] for i in model.most_similar(positive=[system], negative=[sv], topn=50) if i[0].split("_")[1] == "NOUN"][:3]
        return ["Воспользоваться "+i +f" вместо {system.split("_")[0]}" for i in sv_new]
    elif sv not in model and system in model:
        sv_new = [i[0].split("_")[0] for i in model.most_similar(negative=[system], topn=50) if
                  i[0].split("_")[1] == "NOUN"][:3]
        return ["Воспользоваться " + i +f" вместо {system.split("_")[0]}" for i in sv_new]
    return []


def analyze(dictionary):
    results = []
    for f in dictionary["features"]:
        results += parsing(f, dictionary["system"])
    for role in dictionary["roles"]:
        for isp in dictionary["roles"][role]:
            for sv in dictionary["roles"][role][isp]:
                results += parsing(sv, isp)
    for scen in dictionary["scenario"]:
        sp = [process(i) for i in scen.split()]
        if all([i in model for i in sp]):
            results += [ "Подойдет ли вам " + i[0].split("_")[0] +"?" for i in model.most_similar(positive=list(set(sp)), topn=10) if
                  i[0].split("_")[1] == "NOUN"][:3]
    sp = [process(i) for i in dictionary["description"].split()]
    if all([i in model for i in sp]):
        results += [ "Подойдет ли вам " +i[0].split("_")[0]  +"?" for i in model.most_similar(positive=list(set(sp)), topn=10) if
                  i[0].split("_")[1] == "NOUN" ][:3]
    return results



