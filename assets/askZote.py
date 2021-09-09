import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from gensim.models import KeyedVectors
import random

stops = set(stopwords.words("english"))
vectors = KeyedVectors.load("assets/text8vectors.wordvectors", mmap='r')
remove = dict.fromkeys(map(ord, string.punctuation))

fullPreceptsMap = dict()
basicPreceptsMap = dict()

i = 1
with open("assets/precepts") as f:
    for precept in f:
        precept = precept.strip()
        mainText = precept[precept.index(":")+3:].translate(remove)
        basicPreceptsMap[i] = [w for w in mainText.lower().split() if w not in stops]
        fullPreceptsMap[i] = precept[:precept.index(".")+1]+"\n"+precept[precept.index(".")+2:]
        i+=1

def randomPrecept():
    return fullPreceptsMap[random.randint(1, 57)]

def zoteAnswer(question):
    questionWords = question.lower().translate(remove).split()
    questionWords = [qw for qw in questionWords if qw not in stops]
    distances = [vectors.wmdistance(questionWords, basicPreceptsMap[x]) for x in range(1, 57)]
    return fullPreceptsMap[min(basicPreceptsMap.keys(), key=lambda x: vectors.wmdistance(questionWords, basicPreceptsMap[x]))]
