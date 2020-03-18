"""
简单的中缀表达式转前缀/后缀表达式

只有四则运算,没有括号
"""


# a = "1 + 2 * 3"
# + 1 * 2 3
def transform_middle_to_prefix(expression):
    """中缀表达式转前缀表达式"""
    expression = expression.replace(' ', '')

    symbol_priority = {'*': 10, '/': 10, '+': 1, '-': 1}
    new_expression = ''
    symbol_stack = []

    for i in range(len(expression) - 1, -1, -1):  # 逆序遍历字符串
        item = expression[i]
        if item.isdigit():
            new_expression += item
        else:
            top_symbol_stack_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0
            current_symbol_priority = symbol_priority[item]
            while top_symbol_stack_priority > current_symbol_priority:  # 因为是逆序比较, 当两个操作符同优先级时,
                top_symbol = symbol_stack.pop()  # 当前的的操作符在原始字符串中更靠前,栈顶的操作符在字符串中更靠后,
                new_expression += top_symbol  # 所以当前操作符应该先于栈顶操作符加入字符串

                top_symbol_stack_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0
            else:
                symbol_stack.append(item)

    # 至此, 表达式所有元素已经遍历完毕,操作符栈中剩下的都是同级别的操作符,依次弹出加入字符串.
    while len(symbol_stack) != 0:
        last_symbol = symbol_stack.pop()
        new_expression += last_symbol

    # 因为是逆序遍历的字符串,因此还需要再次翻转一下字符串.
    finally_str = ''
    for i in range(len(new_expression) - 1, -1, -1):
        finally_str += new_expression[i]
    return finally_str


if __name__ == '__main__':
    a = "1 + 2 * 3"
    assert transform_middle_to_prefix(a) == '+1*23'

    a = "1 + 2 * 3 - 4"
    assert transform_middle_to_prefix(a) == '-+1*234'

    a = "1 / 2 * 3 - 4 * 5"
    assert transform_middle_to_prefix(a) == '-*/123*45'

