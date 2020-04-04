"""
归并排序
"""
import random


class MergingSort:

    @staticmethod
    def merge(left_part, right_part):
        merged_array = []
        left_index = right_index = 0

        while left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index] > right_part[right_index]:
                merged_array.append(right_part[right_index])
                right_index += 1
            else:
                merged_array.append(left_part[left_index])
                left_index += 1

        merged_array.extend(right_part[right_index:])
        merged_array.extend(left_part[left_index:])

        return merged_array

    @classmethod
    def process(cls, array):
        if len(array) == 1:  # 当长度为1时,表示已经分割至极点,无法再继续分割了
            return array

        middle = len(array) // 2
        left_part = cls.process(array[:middle])
        right_part = cls.process(array[middle:])
        return cls.merge(left_part, right_part)


if __name__ == '__main__':
    a = [i for i in range(16)]
    random.shuffle(a)
    print(MergingSort.process(a))
