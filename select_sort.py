"""
选择排序
"""
import random


class SelectSort:

    @staticmethod
    def process(array):
        array_length = len(array)
        for i in range(array_length):
            min_index = i  # 设置一个游标,记录最小值/最大值的 索引
            for j in range(i + 1, array_length):
                if array[min_index] > array[j]:
                    min_index = j

            if min_index != i:
                array[min_index], array[i] = array[i], array[min_index]

        return array


if __name__ == '__main__':
    a = [i for i in range(15)]
    random.shuffle(a)
    print(a)
    print(SelectSort.process(a))
