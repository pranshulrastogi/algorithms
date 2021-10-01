"""
tests to test merge_sort.py in algorithms/sorting
"""
import os
import sys

_path_to_project = os.path.join(
    os.environ["HOME"], "Desktop", "my_projects", "algorithms"
)
sys.path.append(_path_to_project)
# import test_update_path
import random
from sorting import merge_sort
import unittest

_SORTED_LIST1 = [-1, 2, 4, 5, 6, 8]
_SORTED_LIST2 = [1, 3, 3, 4, 9, 100, 200, 300]
_MERGED_LIST = [-1, 1, 2, 3, 3, 4, 4, 5, 6, 8, 9, 100, 200, 300]


class TestMergeSort(unittest.TestCase):
    def test_merge(self):
        merged_list = merge_sort.merge(_SORTED_LIST1, _SORTED_LIST2)
        self.assertEqual(merged_list, _MERGED_LIST)

    def test_merge_sort(self):
        merged_list = _SORTED_LIST1 + _SORTED_LIST2
        sorted_list = sorted(merged_list)
        length = len(merged_list)
        sorted_by_merge_sort_list = merge_sort.merge_sort(merged_list, 0, length - 1)
        self.assertEqual(sorted_list, sorted_by_merge_sort_list)

    def test_sort(self):
        sorted_list = sorted(_MERGED_LIST)
        output = merge_sort.sort(_SORTED_LIST1 + _SORTED_LIST2)
        self.assertEqual(sorted_list, output)


if __name__ == "__main__":
    unittest.main()
