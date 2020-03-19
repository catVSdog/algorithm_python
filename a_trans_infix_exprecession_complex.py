"""
中缀转前缀/后缀表达式
"""


def trans_infix_prefix(expression):
    """
    中缀转前缀
    1.逆向遍历字符串
    2.如果是数字直接加入结果字符串
    3.如果时非数字
        3.1 如果是 ) 直接加入栈中,要将 ) 的优先级设置为最低, 以便其它操作符加入栈中
        3.2 如果是 (  逐个弹出栈中的元素,直到 )
        3.3 如果不是 ( 和 ), 那么就按简单的运算符进行操作: 如果栈顶运算符有优先级 大于当 前运算符优先级,弹出栈顶操作符,然后继续比较当前操作符和栈顶操作符。。
    4.再次翻转字符串
    """
    expression = expression.replace(' ', '')
    symbol_priority = {'*': 10, '/': 10, '+': 5, '-': 5, '(': 0, ')': 0}
    symbol_stack = []
    new_expression = ''

    for i in range(len(expression) - 1, -1, -1):
        item = expression[i]

        if item.isdigit():
            new_expression += item
        else:
            while True:
                top_symbol_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0
                current_symbol_priority = symbol_priority[item]
                if item == ')':
                    symbol_stack.append(item)
                    break
                elif item == '(':
                    top_symbol = symbol_stack.pop()
                    if top_symbol != ')':
                        new_expression += top_symbol
                    else:
                        break
                elif top_symbol_priority > current_symbol_priority:  # 如果栈顶操作符 > 当前操作符, 那么弹出栈顶操作符,继续循环,比较更新后的栈顶操作符和当前操作符
                    top_symbol = symbol_stack.pop()
                    new_expression += top_symbol
                else:
                    symbol_stack.append(item)
                    break

    while len(symbol_stack) != 0:
        top_symbol = symbol_stack.pop()
        new_expression += top_symbol

    finally_str = ''
    for i in range(len(new_expression) - 1, -1, -1):
        finally_str += new_expression[i]
    return finally_str


def trans_infix_postfix(expression):
    """
    中缀转后缀
    """
    expression = expression.replace(' ', '')
    symbol_priority = {'*': 10, '/': 10, '+': 5, '-': 5, '(': 0, ')': 0}
    symbol_stack = []
    new_expression = ''
    for i in expression:
        if i.isdigit():
            new_expression += i
        else:
            while True:
                top_symbol_priority = symbol_priority[symbol_stack[len(symbol_stack) - 1]] if len(symbol_stack) else 0
                current_symbol_priority = symbol_priority[i]
                if i == '(':
                    symbol_stack.append(i)
                    break
                elif i == ')':
                    symbol = symbol_stack.pop()
                    if symbol != '(':
                        new_expression += symbol
                    else:
                        break
                elif top_symbol_priority >= current_symbol_priority:
                    symbol = symbol_stack.pop()
                    new_expression += symbol
                else:
                    symbol_stack.append(i)
                    break

    while len(symbol_stack) != 0:
        top_symbol = symbol_stack.pop()
        new_expression += top_symbol

    return new_expression


if __name__ == '__main__':
    a = '2 * (1 + 2 * 3) / (3 - 1)'
    assert trans_infix_prefix(a) == '/*2+1*23-31'
    assert trans_infix_postfix(a) == '2123*+*31-/'

    a = '(2 + 1) * 3 + 4 * (2 - 3 * (2 + 1)) + 5'
    assert trans_infix_prefix(a) == '++*+213*4-2*3+215'
    assert trans_infix_postfix(a) == '21+3*42321+*-*+5+'

    a = '1 + (2 + 3) * 4 - 5'
    assert trans_infix_prefix(a) == '-+1*+2345'
    assert trans_infix_postfix(a) == '123+4*+5-'
