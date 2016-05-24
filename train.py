from Corpus import Corpus
from MCP import MulticlassPerceptron
from Training import Training

training = Training(MulticlassPerceptron(Corpus("dev1.col")))
training.train(3, "check.col")
