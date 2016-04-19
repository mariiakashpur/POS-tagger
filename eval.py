from Token import Token
from Sentence import Sentence
from Corpus import Corpus
from Evaluation import Evaluation


print Evaluation(Corpus("dev.col","dev-predicted.col")).evaluate()