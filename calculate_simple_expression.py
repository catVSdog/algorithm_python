"""
计算简单表达式
只有四则运算,没有括号
"""


def calculate_simple_expression(expression):
    expression = expression.replace(' ', '')
    symbol_priority = {'*': 10, "/": 10, "+": 1, "-": 1}
    isdigit_stack = []  # 数字栈
    symbol_stack = []  # 操作符栈

    for i in expression:
        if i.isdigit():
            isdigit_stack.append(i)
        else:
            symbol_top_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0  # 操作符栈顶符号优先级,如果栈为空,优先级为0
            current_symbol_priority = symbol_priority[i]  # 当前操作符优先级
            while symbol_top_priority >= current_symbol_priority:  # 当栈顶操作符优先级 大于或等于 仓前操作符优先级时,要弹出栈顶操作符并且进行计算
                first_number = isdigit_stack.pop()  # 弹出数字栈的栈顶元素
                second_number = isdigit_stack.pop()  # 再次弹出数字栈的栈顶元素
                symbol = symbol_stack.pop()  # 弹出操作符栈的栈顶元素
                sum_two_number = eval(f'{second_number}{symbol}{first_number}')  # 注意： 对于 / 和 -  操作数的位置非常重要.
                isdigit_stack.append(sum_two_number)  # 将计算结果重新放入数字栈中

                symbol_top_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0  # 再次计算操作符栈栈顶元素的优先级
            else:
                symbol_stack.append(i)

    # 至此,表达式全部元素都已经遍历完了,不会再有向栈中添加元素的操作了,因此 两个栈中的元素可以持续的弹出,计算,弹出,计算...直到所有的操作符都用完
    finally_number = 0
    while len(symbol_stack) != 0:  # 以操作栈是否为空来判定是否继续计算.毕竟操作数的数量总会多余操作符的数量
        first_number = isdigit_stack.pop()  # 栈顶元素其实是后入栈的
        second_number = isdigit_stack.pop()  # 栈的第二个元素其实比栈顶元素先入栈.
        current_symbol = symbol_stack.pop()

        finally_number = eval(f'{second_number}{current_symbol}{first_number}')  # 注意： 对于 / 和 -  操作数的位置非常重要.
        isdigit_stack.append(finally_number)

    return finally_number


if __name__ == '__main__':
    a = "1 / 2 - 3 + 4 / 2"
    assert calculate_expression(a) == eval(a)
    a = "1 - 2 * 3 + 4 / 2"
    assert calculate_expression(a) == eval(a)
    a = "1 + 2 * 3 + 4 / 2"
    assert calculate_expression(a) == eval(a)
    a = "1 + 2 * 3 + 4 - 2"
    assert calculate_expression(a) == eval(a)
    a = "1 + 1 + 1 + 1 + 1"
    assert calculate_expression(a) == eval(a)
    a = "4 / 2"
    assert calculate_expression(a) == eval(a)
    a = "1 - 4 / 2"
    assert calculate_expression(a) == eval(a)

