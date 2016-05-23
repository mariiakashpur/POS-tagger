<<<<<<< HEAD
from Corpus import Corpus
from MCP import MulticlassPerceptron
from Training import Training

training = Training(MulticlassPerceptron(Corpus("dev1.col")))
training.train(5)
prediction = training.predict(Corpus("check.col"))
print prediction
#training.createOutputFile(prediction, "output.txt")
=======
#!/usr/bin/env python

from Token import Token
from Sentence import Sentence
from Corpus import Corpus
from Evaluation import Evaluation
import sys

corpus = Corpus()
>>>>>>> 1ed2340993c46ee93a48cdaed17f74e2c2a93331
