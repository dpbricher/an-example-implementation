class Point2d:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def add(self, x=0, y=0):
    self.x += x
    self.y += y

    return self

  def clone(self):
    return Point2d(self.x, self.y)

  def __eq__(self, targetPoint):
    return (self.x, self.y) == (targetPoint.x, targetPoint.y)

  def __str__(self):
    return f'({self.x},{self.y})'
