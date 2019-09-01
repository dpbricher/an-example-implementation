#!/usr/bin/env python3
import sys
from find import find_paths

if (len(sys.argv) < 3):
  print(f'Usage: {sys.argv[0]} GRID_STRING TARGET_POINT')
  exit(1)

gridRows = sys.argv[1].strip('|').split('|')
gridList = []

for row in gridRows:
  numbers = row.split(',')
  gridList.append(tuple(int(n) for n in numbers))

target = tuple(int(n) for n in sys.argv[2].split(','))

pathList = find_paths(gridList, target)
pathCount = len(pathList)

print(f'Found {pathCount} paths{":" if pathCount > 0 else ""}')

for i, path in enumerate(pathList):
  print(f'#{i + 1}: {path.directions()}')
