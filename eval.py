from Token import Token
from Sentence import Sentence
from Corpus import Corpus
from Evaluation import Evaluation

print Evaluation(Corpus("dev1.col","dev-predicted1.col")).format()