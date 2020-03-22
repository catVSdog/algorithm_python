"""
后缀表达式计算
从左到右遍历
1.如果时数字,入栈
2.非数字, 将两个数字出栈,计算之后将计算结果入栈
"""


def calculate_exprecession(exprecession):
    exprecession = exprecession.replace(' ', '')
    cal_two_number = 0
    number_stack = []
    for i in exprecession:
        if i.isdigit():
            number_stack.append(i)
        else:
            first_number = number_stack.pop()
            second_number = number_stack.pop()
            cal_two_number = eval(f'{second_number}{i}{first_number}')  # 注意操作数的顺序
            number_stack.append(cal_two_number)

    return cal_two_number


if __name__ == '__main__':
    a = '2123*+*31-/'
    assert calculate_exprecession(a) == eval('2 * (1 + 2 * 3) / (3 - 1)')

    a = '21+3*42321+*-*+5+'
    assert calculate_exprecession(a) == eval('(2 + 1) * 3 + 4 * (2 - 3 * (2 + 1)) + 5')

    a = '123+4*+5-'
    assert calculate_exprecession(a) == eval('1 + (2 + 3) * 4 - 5')

    a = '12+'
    assert calculate_exprecession(a) == 3
