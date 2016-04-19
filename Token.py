class Token: 

  def __init__(self, text, goldPOS, predictedPOS):
    self.text = text
    self.goldPOS = goldPOS
    self.predictedPOS = predictedPOS

  def getText(self):
    return self.text

  def getGoldPOS(self):
    return self.goldPOS

  def getPredictedPOS(self):
    return self.predictedPOS

  def isLabeledCorrectly(self):
    return self.goldPOS == self.predictedPOS









    
