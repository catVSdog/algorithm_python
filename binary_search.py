"""
二分查找
序列中的数据必须时有序的
"""


def BinarySearch(target, array, begin, end):
    if begin > end:
        return -1
    mid = (begin + end) // 2

    if array[mid] > target:
        return BinarySearch(target, array, begin, mid -1)
    if array[mid] < target:
        return BinarySearch(target, array, mid + 1, end)
    return mid



if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 21, 33, 45, 67, 89]
    print(BinarySearch(10, a, 0, len(a)-1))