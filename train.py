from Corpus import Corpus
from MCP import MulticlassPerceptron
from Training import Training

training = Training(MulticlassPerceptron(Corpus("train.col")))
training.train(50, "test.col")