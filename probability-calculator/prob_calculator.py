import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []

    for k,v in kwargs.items():
      self.contents.extend([k for i in range(v)])

  def draw(self, num):
    index = 0
    drawn = []
    
    if num >= len(self.contents):
      return self.contents
    
    while index < num:
      ball = self.contents.pop(int(random.randrange(len(self.contents))))
      drawn.append(ball)
      
      index += 1

    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  index = 0
  succ_count = 0.0

  while index < num_experiments:
    copied_hat = copy.deepcopy(hat)
    drawn_balls = copied_hat.draw(num_balls_drawn)
    
    expected = []
    for k,v in expected_balls.items():
      expected.extend([k for i in range(v)])
    
    if test(drawn_balls, expected):
      succ_count += 1
  
    index += 1
    
  return succ_count/num_experiments

def test(drawn_balls, expected):
  for ball in expected:
    if ball in drawn_balls:
      drawn_balls.remove(ball)
    else:
      return False
  return True