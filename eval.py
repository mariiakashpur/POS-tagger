from Token import Token
from Sentence import Sentence
from Corpus import Corpus
from Result import Result


evaluation = Result(Corpus("dev.col","dev-predicted.col").getSentStats())

print evaluation.Evaluation()



    
