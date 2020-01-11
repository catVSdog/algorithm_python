"""
朴素字符串匹配
"""


def search_string(target, source):
    i = 0  # source 主串索引
    j = 0  # target 子串索引
    target_len = len(target)
    source_len = len(source)

    while i < source_len and j < target_len:  # 当 i, j 两个 索引均未超出最大索引值的时候,持续遍历,
        if source[i] == target[j]:  # 如果 target 和 source 相应索引的值相等,那么就分别移动两个字符串的指针
            i += 1  # 使其 各自 向后挪一位,
            j += 1  # 然后接着比较,　不断循环
        else:  # 如果不相等...
            i = i - j + 1  # j 的作用不仅仅是target的索引,target正在参与比较的值的指针,同时记载了每一轮循环,source(和target)到目前为止已经比较了多少个字符了了,起到一个计数的作用.
            j = 0  # i 没办法起到计数的作用,因为i是持续不断的增长的.而j每次循环都会重置. 此处让i-j 就是让i回归本次循环的起始点,
            # 然后再 +1,即从本轮起始位的下一位重新开始一轮新的比较.同时将j重置为0.

    if j >= target_len:  # 当j == target_len时,说明target所有的字符串都已经比较完了,且都在source中找到了相应的值
        return i - j  # j 起到计数的作用.即：本轮循环比较了多少个字符串,i-j 即可得到本轮i的起始位置,也就是主串和子串开始匹配的位置.当然 也可以写成 i-target_len
    else:  # 当i超过了最大索引值,说明已经匹配完了,既然已经进入此语句,这时候,无论j是多少,都没有意义了,说明没有在主串中找到子串.
        return -1


if __name__ == '__main__':
    source = "goodgoogle"  # length = 10
    target = "google"  # length 6
    print(f"answer is {search_string(target, source)}")
