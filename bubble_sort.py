"""
冒泡排序
"""
import random


class BubbleSort:

    @staticmethod
    def process(array):
        array_length = len(array)
        for i in range(array_length - 1, -1, -1):
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    @staticmethod
    def process_enhance(array):
        array_length = len(array)
        for i in range(array_length - 1, -1, -1):
            flag = False  # 标识位-本次循环是否进行了数据交换
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    flag = True
            if flag is False:
                break
        return array


if __name__ == '__main__':
    a = [i for i in range(14)]
    random.shuffle(a)
    print(a)
    print(BubbleSort.process_enhance(a))
