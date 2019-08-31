class GridPath(tuple):
  def directions(self):
    dirList = []

    for i, p in enumerate(self[1:]):
      if p.x > self[i].x:
        dirList.append('R')
      else:
        dirList.append('D')

    return '>'.join(dirList)

  def extend(self, point):
    return GridPath(self + (point,))

  def last(self):
    return self[-1]

  def __str__(self):
    return '>'.join(str(s) for s in self)
