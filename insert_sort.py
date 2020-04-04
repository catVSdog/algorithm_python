"""
插入排序
"""
import random
from copy import deepcopy


class InsertSort:

    @staticmethod
    def straight_sort(array):
        """直接插入排序"""
        array_length = len(array)
        for disorder_index in range(1, array_length):
            moving_node = array[disorder_index]
            order_max_index = disorder_index - 1

            while order_max_index >= 0 and array[order_max_index] > moving_node:  # 向左移动,挨个进行比较,直到数组的第一个元素,也就是索引为0的元素
                array[order_max_index + 1] = array[order_max_index]
                order_max_index -= 1

            array[order_max_index + 1] = moving_node
        return array

    @staticmethod
    def binary_sort(array):
        """折半插入"""
        array_length = len(array)

        for disorder_index in range(1, array_length):
            begin = 0
            end = disorder_index - 1
            moving_node = array[disorder_index]

            while begin <= end:
                mid = (begin + end) // 2
                if array[mid] > moving_node:
                    end = mid - 1
                else:
                    begin = mid + 1

            print(f'begin: {begin}')  # 程序运行至此, begin 总是比 end 大1
            print(f'end: {end}')

            for order_index in range(disorder_index - 1, end, -1):
                array[order_index + 1] = array[order_index]

            array[begin] = moving_node
        return array


if __name__ == '__main__':
    a = [i for i in range(15)]
    random.shuffle(a)
    print(a)
    assert InsertSort.straight_sort(deepcopy(a)) == InsertSort.binary_sort(deepcopy(a))
