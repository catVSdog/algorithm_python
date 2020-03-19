"""
简单的中缀表达式转前缀/后缀表达式

只有四则运算,没有括号
"""


def transform_infix_to_prefix(expression):
    """
    中缀表达式转前缀表达式
    1.翻转字符串进行遍历
    2.操作数直接加入结果字符串
    3.栈顶元素** 大于 ** 当前元素时才出栈,加入结果字符串
    4.翻转结果字符串
    """
    expression = expression.replace(' ', '')

    symbol_priority = {'*': 10, '/': 10, '+': 1, '-': 1}
    new_expression = ''
    symbol_stack = []

    for i in range(len(expression) - 1, -1, -1):  # 逆序遍历字符串
        item = expression[i]
        if item.isdigit():
            new_expression += item
        else:
            top_symbol_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0
            current_symbol_priority = symbol_priority[item]
            while top_symbol_priority > current_symbol_priority:  # 因为是逆序比较, 当两个操作符同优先级时,
                top_symbol = symbol_stack.pop()  # 当前的的操作符在原始字符串中更靠前,栈顶的操作符在原始字符串中更靠后,
                new_expression += top_symbol
                # 更新栈顶操作符的优先级. 以便当前操作符继续和栈顶操作符比较,如果栈顶操作符优先级 > 当前操作符优先级,那么继续弹出..
                top_symbol_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0
            else:
                symbol_stack.append(item)  # 所以当前操作符应该先入栈,从而实现在出栈的时候,先出栈

    # 至此, 表达式所有元素已经遍历完毕,操作符栈中剩下的都是同级别的操作符,依次弹出加入字符串.
    while len(symbol_stack) != 0:
        last_symbol = symbol_stack.pop()
        new_expression += last_symbol

    # 因为是逆序遍历的字符串,因此还需要再次翻转一下字符串.
    finally_str = ''
    for i in range(len(new_expression) - 1, -1, -1):
        finally_str += new_expression[i]
    return finally_str


def transform_infix_to_postfix(expression):
    """
    中缀转后缀
    1.遍历字符串,数字直接加到结果字符串
    2.如果是操作符, 如果栈顶操作符优先级 大于等于 当前操作符优先级,那么栈顶操作符先出栈,
        然后将当前操作符再次和更新之后的栈顶操作符比较,如果更新后的栈顶操作符优先级 大于等于 当前操作符优先级,那么栈顶操作符先出栈,否则入栈
    """
    expression = expression.replace(' ', '')
    new_expression = ''
    symbol_stack = []
    symbol_priority = {'*': 10, '/': 10, '+': 1, '-': 1}

    for i in expression:
        if i.isdigit():
            new_expression += i
        else:
            top_symbol_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0
            current_symbol_priority = symbol_priority[i]

            while top_symbol_priority >= current_symbol_priority:  # 因为我们是顺序遍历,同优先级的操作符理应排在前面
                pop_symbol = symbol_stack.pop()
                new_expression += pop_symbol
                # 更新栈顶操作符的优先级. 以便当前操作符继续和栈顶操作符比较,如果栈顶操作符优先级 >= 当前操作符优先级,那么继续弹出..
                top_symbol_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0
            else:
                symbol_stack.append(i)

    # 至此, 表达式所有元素已经遍历完毕,操作符栈中剩下的都是同级别的操作符,依次弹出加入字符串.
    while len(symbol_stack) != 0:
        pop_symbol = symbol_stack.pop()
        new_expression += pop_symbol

    return new_expression


if __name__ == '__main__':
    a = "1 + 2 * 3"
    assert transform_infix_to_prefix(a) == '+1*23'
    assert transform_infix_to_postfix(a) == '123*+'

    a = "1 + 2 * 3 - 4"
    assert transform_infix_to_prefix(a) == '-+1*234'
    assert transform_infix_to_postfix(a) == '123*+4-'

    a = "1 / 2 * 3 - 4 * 5"
    assert transform_infix_to_prefix(a) == '-*/123*45'
    assert transform_infix_to_postfix(a) == '12/3*45*-'

    a = "1 + 2 - 3"
    assert transform_infix_to_prefix(a) == '-+123'
    assert transform_infix_to_postfix(a) == '12+3-'
