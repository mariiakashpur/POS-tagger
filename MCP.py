from __future__ import division
from collections import Counter, defaultdict
<<<<<<< HEAD
from random import shuffle
import math
from Perceptron import Perceptron
=======
import math
from Perceptron import Perceptron
from Token import Token
from nltk.data import load # to get penn tags

>>>>>>> 1ed2340993c46ee93a48cdaed17f74e2c2a93331


class MulticlassPerceptron(object): 

<<<<<<< HEAD
  def __init__(self, corpus):
    self.perceptrons = {}
    for tag in corpus.getTags():
      self.perceptrons[tag.strip()] = Perceptron(tag.strip())
    self.corpus = corpus

  @staticmethod
  def getDefaultTag():
    return "NN"
=======
  def __init__(self):
    self.perceptrons = {}
    for tag in load('help/tagsets/upenn_tagset.pickle').keys():
      self.perceptrons[tag] = Perceptron(tag)
>>>>>>> 1ed2340993c46ee93a48cdaed17f74e2c2a93331

  def getPerceptronFromTag(self, tag):
    return self.perceptrons[tag]

  def getBestTag(self, token):
    currentBestScore = 0.0
<<<<<<< HEAD
    currentBestTag = self.getDefaultTag()
    for perceptron in self.perceptrons:
      if self.perceptrons[perceptron].getScore(token) > currentBestScore:
        currentBestScore = self.perceptrons[perceptron].getScore(token)
        currentBestTag = self.perceptrons[perceptron].getTag()
    return currentBestTag

  def train(self):
    for sent in self.corpus.getSents():
      for token in sent.getTokens():
        predictedTag = self.getBestTag(token)
        if predictedTag == token.getGoldPOS():
          continue
        else:
          self.getPerceptronFromTag(predictedTag).reduceWeights(token)
          self.getPerceptronFromTag(token.getGoldPOS().strip()).increaseWeights(token)

  # def train(self):
  #   for token in self.corpus.randomTokens():
  #     predictedTag = self.getBestTag(token)
  #     if predictedTag == token.getGoldPOS():
  #       continue
  #     else:
  #       self.getPerceptronFromTag(predictedTag).reduceWeights(token)
  #       self.getPerceptronFromTag(token.getGoldPOS().strip()).increaseWeights(token)






=======
    currentBestTag = "NN"
    for perceptron in self.perceptrons:
      if perceptron.getScore() > currentBestScore:
        currentBestScore = perceptron.getScore()
        currentBestTag = perceptron.getTag()
    return currentBestTag
>>>>>>> 1ed2340993c46ee93a48cdaed17f74e2c2a93331
