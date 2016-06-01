from Corpus import Corpus
from MCP import MulticlassPerceptron
from Training import Training

training = Training(MulticlassPerceptron(Corpus("train.col")))
training.train(20, "dev.col")
