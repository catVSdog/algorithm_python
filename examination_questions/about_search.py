def minArray(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        elif nums[mid] < nums[r]:
            r = mid
        else:
            r -= 1
    return nums[r]


if __name__ == '__main__':
    a = [1, 1, 1, 1, 1, 0, 1, 1]

    print(minArray(a))