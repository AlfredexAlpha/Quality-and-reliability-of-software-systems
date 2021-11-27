import spacy
import textacy
from textacy import extract
import textacy.datasets

use_lang = 'en_core_web_lg'
doc = textacy.make_spacy_doc(text, lang=use_lang)

ds = textacy.datasets.CapitolWords()
ds.download()
corpus = textacy.Corpus(lang=en, data=ds.texts(speaker_party="R", chamber="House", limit=100))
print(corpus)
print(corpus.n_docs, corpus.n_sents, corpus.n_tokens)

# get keywords
def get_keywords(corpus, min_rank = 0.03, max_feat = 20):
    kw = (extract.keyterms.textrank(doc, normalize="lower", window_size=2, edge_weighting="binary", topn=max_feat) for doc in corpus)
    kw_dict = {}

    for index, k in enumerate(kw):
        k2 = [i for i in k if i[1] > min_rank]
        kw_dict.update({index: k2})
      
    return kw_dict

def get_unique_keywords(kw_dict):
    s = set()
    for keys, i in kw_dict.items():
        for j in i:
            s.add(j[0])
    return s

kw_dict = get_keywords(corpus, min_rank = 0.1)
kw_unique = get_unique_keywords(kw_dict)
print(len(kw_unique))

for rank in kw_unique:
    print(dic)