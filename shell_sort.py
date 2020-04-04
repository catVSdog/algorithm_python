"""
希尔排序
"""
import random


class ShellSort:

    @staticmethod
    def process(array):
        array_length = len(array)

        step = array_length // 2

        while step > 0:
            for disorder_index in range(step, array_length):
                moving_node = array[disorder_index]
                order_max_index = disorder_index - step

                while order_max_index >= 0 and moving_node < array[order_max_index]:
                    array[order_max_index + step] = array[order_max_index]
                    order_max_index -= step
                array[order_max_index + step] = moving_node
            step = step // 2
        return array


if __name__ == '__main__':
    a = [i for i in range(15)]
    random.shuffle(a)
    print(a)
    print(ShellSort.process(a))
