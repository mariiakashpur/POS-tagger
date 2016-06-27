from __future__ import division
from collections import Counter, defaultdict
import random
import math
from Perceptron import Perceptron



class MulticlassPerceptron(object): 

  def __init__(self, corpus):
    self.perceptrons = {}
    # !!! make separate method for batch learning 
    self.intermPerceptrons = {} #BATCH LEARNING
    for tag in corpus.getTags():
      cleanTag = tag.strip()
      self.perceptrons[cleanTag] = Perceptron(cleanTag)
      self.intermPerceptrons[cleanTag] = Perceptron(cleanTag) # !!! why not set self.intermPerceptrons = self.perceptrons after for loop?
    self.corpus = corpus

  @staticmethod
  def getDefaultTag():
    return "NN"

  def getPerceptronFromTag(self, tag):
    return self.perceptrons[tag]

  def getIntermPerceptronFromTag(self, tag):
    return self.intermPerceptrons[tag]

  def getBestTag(self, token):
    currentBestScore = 0.0
    currentBestTag = self.getDefaultTag()
    for perceptron in self.perceptrons:
      currentPerceptron = self.perceptrons[perceptron]
      currentScore = currentPerceptron.getScore(token)
      if currentScore > currentBestScore:
        currentBestScore = currentScore
        currentBestTag = currentPerceptron.getTag()
    return currentBestTag

  def train(self):
    for sent in self.corpus.getSents():
      for token in random.sample(sent.getTokens(), len(sent.getTokens())):
        predictedTag = self.getBestTag(token)
        token.setPredictedPOS(predictedTag) # !!! we do the same action in Training::setPredictedTags() ?
        if predictedTag == token.getGoldPOS():
          continue
        else:
          self.getIntermPerceptronFromTag(predictedTag).reduceWeights(token)
          self.getIntermPerceptronFromTag(token.getGoldPOS().strip()).increaseWeights(token)
    self.perceptrons = self.intermPerceptrons

          # self.getPerceptronFromTag(predictedTag).reduceWeights(token)
          # self.getPerceptronFromTag(token.getGoldPOS().strip()).increaseWeights(token)

  


