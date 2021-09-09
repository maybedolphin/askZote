from gensim.models import Word2Vec
import gensim.downloader as api

corpus = api.load('text8')
model = Word2Vec(corpus)
model.wv.save("text8vectors.wordvectors")
