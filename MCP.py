from __future__ import division
from collections import Counter, defaultdict
import math
from Perceptron import Perceptron
from Token import Token
from nltk.data import load # to get penn tags



class MulticlassPerceptron(object): 

  def __init__(self):
    self.perceptrons = {}
    for tag in load('help/tagsets/upenn_tagset.pickle').keys():
      self.perceptrons[tag] = Perceptron(tag)

  def getBestTag(self, token):
    currentBestScore = 0.0
    currentBestTag = "NN"
    for perceptron in self.perceptrons:
      if perceptron.getScore() > currentBestScore:
        currentBestScore = perceptron.getScore()
        currentBestTag = perceptron.getTag()
    return currentBestTag

