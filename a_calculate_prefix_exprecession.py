"""
前缀表达式计算
从 右到左 遍历

1.如果时数字,入栈
2.非数字, 将两个数字出栈,计算之后将计算结果入栈
"""


def calculate_exprecession(exprecession):
    exprecession = exprecession.replace(' ', '')
    cal_two_number = 0
    numbuer_stack = []

    for i in range(len(exprecession) - 1, -1, -1):
        item = exprecession[i]

        if item.isdigit():
            numbuer_stack.append(item)
        else:
            first_number = numbuer_stack.pop()
            second_number = numbuer_stack.pop()
            cal_two_number = eval(f'{first_number}{item}{second_number}')  # 注意操作数的顺序
            numbuer_stack.append(cal_two_number)

    return cal_two_number


if __name__ == '__main__':
    a = '/*2+1*23-31'
    assert calculate_exprecession(a) == eval('2 * (1 + 2 * 3) / (3 - 1)')

    a = '++*+213*4-2*3+215'
    assert calculate_exprecession(a) == eval('(2 + 1) * 3 + 4 * (2 - 3 * (2 + 1)) + 5')

    a = '-+1*+2345'
    assert calculate_exprecession(a) == eval('1 + (2 + 3) * 4 - 5')
