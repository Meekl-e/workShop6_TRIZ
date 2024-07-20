
from gensim.models import KeyedVectors
from ufal.udpipe import Model, Pipeline


model = KeyedVectors.load_word2vec_format("model.bin", binary=True)
mod = Model.load('udpipe_syntagrus.model')
pipeline = Pipeline(mod, 'tokenize', Pipeline.DEFAULT, Pipeline.DEFAULT, 'conllu')

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


def parsing(sv, system):
    system = process(system)

    sv = process(sv)
    if system in model and sv in model:
        sv_new =  [i[0].split("_")[0] for i in model.most_similar(positive=[system], negative=[sv], topn=50) if i[0].split("_")[1] == "NOUN"]
        return ["Воспользоваться "+i for i in sv_new]
    elif sv not in model:
        sv_new = [i[0].split("_")[0] for i in model.most_similar(negative=[system], topn=50) if
                  i[0].split("_")[1] == "NOUN"]
        return ["Воспользоваться " + i for i in sv_new]


def analyze(dictionary):
    results = []
    for f in dictionary["features"]:
        results += parsing(f, dictionary["system"])
    for role in dictionary["roles"]:
        for isp in dictionary["roles"][role]:
            for sv in dictionary["roles"][role][isp]:
                results += parsing(sv, isp)
    for scen in dictionary["scenario"]:
        sp = [process(i) for i in dictionary["task"].split()] + [process(i) for i in scen.split()]
        if all([i in model for i in sp]):
            results += [ "Подойдет ли вам " + i[0].split("_")[0] for i in model.most_similar(positive=sp, topn=10) if
                  i[0].split("_")[1] == "NOUN"]
    sp = [process(i) for i in dictionary["description"].split()]
    if all([i in model for i in sp]):
        results += [ "Подойдет ли вам " +i[0].split("_")[0] for i in model.most_similar(positive=sp, topn=10) if
                  i[0].split("_")[1] == "NOUN" ]
    return results



