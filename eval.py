from Token import Token
from Sentence import Sentence
from Corpus import Corpus
from Evaluation import Evaluation

# corp = Corpus("dev.col","dev-predicted.col")
# print Evaluation().getSentStats().evaluate()
print Evaluation(Corpus("dev.col","dev-predicted.col").getSentStats()).evaluate()
#corp = Corpus("dev.col","dev-predicted.col")
#print corp.getSentStats()