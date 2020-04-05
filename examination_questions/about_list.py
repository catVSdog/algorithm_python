def function_a(array):
    """
    从数组中找到重复的数字
    复杂度是 O(n)
    """
    temp_a = {}

    for i in array:
        if i in temp_a:
            temp_a[i] += 1
        else:
            temp_a[i] = 1

    temp_b = {}
    for k, v in temp_a.items():
        if v > 1:
            temp_b[k] = v
    return temp_b


def function_b(array):
    """
    不修改数组,找到重复的数字
    复杂度 O(n)
    """

    temp = [None] * (max(array) + 1)

    for i in array:
        if temp[i] == i:
            return i
        temp[i] = i
    return None


def function_c(matrix, target):
    """
    判断二维数组是否包含target
    复杂度 O(n^2)
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == target:
                return True
    return False


def function_d(matrix, target):
    if matrix == [[]] or matrix == []:
        return False

    if target < matrix[0][0]:
        return False

    row = 0
    col = len(matrix[0]) - 1
    while row <= len(matrix) - 1 and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return True
    return False


if __name__ == '__main__':
    a = [1, 3, 4, 3, 3, 6, 7, 8, 9, 4]
    # print(function_a(a))
    # print(function_b(a))

    a = [
        [1, 2, 3, 4, 5, 6, 7],
        [2, 3, 4, 5, 6, 7, 8],
        [3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 10],
        [5, 6, 7, 8, 9, 10, 11]
    ]
    print(function_d(a, 11))
