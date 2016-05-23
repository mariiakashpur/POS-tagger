from Corpus import Corpus
from MCP import MulticlassPerceptron
from Training import Training

training = Training(MulticlassPerceptron(Corpus("dev1.col")))
training.train(5)
prediction = training.predict(Corpus("check.col"))
print prediction
#training.createOutputFile(prediction, "output.txt")
