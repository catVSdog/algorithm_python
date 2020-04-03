"""
查找
"""
import random
from copy import deepcopy


class Search:
    @staticmethod
    def sequential_search(array, target):
        """顺序查找/线性查找"""
        random.shuffle(array)
        for index in range(len(array)):
            if array[index] == target:
                return index
        return -1

    @classmethod
    def binary_search(cls, array, target, begin, end):
        """折半查找/二分查找 必须有序"""
        if begin > end:
            return -1

        mid = (begin + end) // 2

        if array[mid] > target:
            return cls.binary_search(array, target, begin, mid - 1)
        if array[mid] < target:
            return cls.binary_search(array, target, mid + 1, end)
        return mid

    @staticmethod
    def binary_search_iteration(array, target):
        begin = 0
        end = len(array) - 1

        while begin <= end:  # 注意 begin == end

            if array[begin] == target:  # 判断 begin end 是否等于target 这两行可以省略,只是为了小小优化一下
                return begin
            if array[end] == target:
                return end

            mid = (begin + end) // 2
            if array[mid] > target:
                end = mid - 1
            elif array[mid] < target:
                begin = mid + 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    print(Search.sequential_search(deepcopy(a), 6))
    assert Search.binary_search(a, 7, 0, len(a) - 1) == 7
    assert Search.binary_search_iteration(a, 7) == 7
