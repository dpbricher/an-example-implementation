#!/usr/bin/env python3
import unittest
from find import find_paths

class TestFindPaths(unittest.TestCase):
  def test_excess_paths(self):
    pathList = find_paths((
      (1, 1, 1, 1),
      (1, 0, 1, 0),
      (1, 0, 1, 1),
      (1, 1, 1, 1),
      (1, 0, 1, 1)
    ), (2, 3))

    self.assertEqual(len(pathList), 2)

    dirList = self.__get_dir_list(pathList)

    self.assertTrue('R>R>D>D>D' in dirList)
    self.assertTrue('D>D>D>R>R' in dirList)

  def test_multi_path_one(self):
    pathList = find_paths((
      (1, 1, 1),
      (1, 1, 1),
      (0, 1, 1)
    ), (2, 2))

    self.assertEqual(len(pathList), 5)

    dirList = self.__get_dir_list(pathList)

    self.assertTrue('R>R>D>D' in dirList)
    self.assertTrue('R>D>R>D' in dirList)
    self.assertTrue('R>D>D>R' in dirList)
    self.assertTrue('D>R>R>D' in dirList)
    self.assertTrue('D>R>D>R' in dirList)

  def test_multi_path_two(self):
    pathList = find_paths((
      (1, 1, 1, 1, 1, 1),
      (1, 0, 1, 0, 0, 1),
      (1, 0, 1, 1, 0, 1),
      (1, 0, 1, 1, 0, 1),
      (1, 0, 0, 1, 0, 1),
      (1, 1, 1, 1, 1, 1)
    ), (5, 5))

    self.assertEqual(len(pathList), 4)

    dirList = self.__get_dir_list(pathList)

    self.assertTrue('R>R>R>R>R>D>D>D>D>D' in dirList)
    self.assertTrue('D>D>D>D>D>R>R>R>R>R' in dirList)
    self.assertTrue('R>R>D>D>R>D>D>D>R>R' in dirList)
    self.assertTrue('R>R>D>D>D>R>D>D>R>R' in dirList)

  def test_no_path(self):
    pathList = find_paths((
      (1, 1, 1),
      (1, 0, 0),
      (1, 0, 1)
    ), (2, 2))

    self.assertEqual(len(pathList), 0)

  def test_single_path(self):
    pathList = find_paths((
      (1, 1, 0),
      (0, 1, 0),
      (0, 1, 1)
    ), (2, 2))

    self.assertEqual(len(pathList), 1)
    self.assertEqual(pathList[0].directions(), 'R>D>D>R')

  def test_start_at_path(self):
    pathList = find_paths((
      (1, 1),
      (1, 1)
    ), (0, 0))

    self.assertEqual(len(pathList), 1)
    self.assertEqual(str(pathList[0]), '(0,0)')


  def __get_dir_list(self, pathList):
    return tuple(p.directions() for p in pathList)


if __name__ == '__main__':
  unittest.main()
