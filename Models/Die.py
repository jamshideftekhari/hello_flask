import random

class Die(object): 

 def __init__(self, eye, pic):
  self.FaceValue = eye
  self.FacePic = pic
 
 def roll(self):
  self.FaceValue = random.randint(1,6)
  if self.FaceValue == 1:
    self.FacePic = "images/d1.png"
  elif self.FaceValue == 2:
    self.FacePic = "images/d2.png"  
  elif self.FaceValue == 3:
    self.FacePic = "images/d3.png"
  elif self.FaceValue == 4:
    self.FacePic = "images/d4.png"
  elif self.FaceValue == 5:
    self.FacePic = "images/d5.png"
  elif self.FaceValue == 6:
    self.FacePic = "images/d6.png"


 def GetFaceValue(self):
   return self.FaceValue

 def GetPicLink(self):
   return self.FacePic 