"""
快速排序
"""
import random


class QuickSort:
    @classmethod
    def process(cls, array, begin, end):

        if begin > end:
            return

        cursor_left = begin
        cursor_right = end
        standard_value = array[end]  # 基准值,比起小的放于一边,比其大的放于另一边

        while cursor_left != cursor_right:

            while cursor_left < cursor_right and array[cursor_left] < standard_value:  # 只要比基准值小,就持续移动左侧游标
                cursor_left += 1
            array[cursor_right] = array[cursor_left]

            while cursor_left < cursor_right and array[cursor_right] > standard_value:
                cursor_right -= 1
            array[cursor_left] = array[cursor_right]

        array[cursor_left] = standard_value  # 游标合并地,即为标准值

        cls.process(array, begin, cursor_left - 1)  # 递归处理标准值左右两边
        cls.process(array, cursor_left + 1, end)

        return array


if __name__ == '__main__':
    a = [i for i in range(16)]
    random.shuffle(a)
    print(a)
    print(QuickSort.process(a, 0, len(a) - 1))
