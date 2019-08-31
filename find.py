from point import Point2d
from path import GridPath

def find_paths(binaryGrid, targetTuple=(0, 0)):
  targetPoint = Point2d(*targetTuple)

  checkedList = []
  nextList = [ GridPath((Point2d(0, 0),)) ]

  while len(nextList) > 0:
    currentPath = nextList.pop()
    currentPos = currentPath.last()

    checkedList.append(currentPath)

    for point in (currentPos.clone().add(1), currentPos.clone().add(0, 1)):
      if point.y in range(0, len(binaryGrid)) and point.x in range(0, len(binaryGrid[point.y])) and binaryGrid[point.y][point.x] == 1:
        newPath = currentPath.extend(point)
        nextList.append(newPath)

  return tuple(p for p in checkedList if p.last() == targetPoint)
