"""
平衡符号问题

要求符号必须成对出现.
属于栈的应用
"""


def symbol_balance(string):
    stack = []
    string = string.replace(' ', '')
    symbol = {'(':')', '{':'}', '[':']'}
    for i in string:
        if i in symbol.keys():
            stack.append(i)
        elif i in symbol.values():
            if len(stack) == 0:
                return False
            else:
                top_symbol = stack.pop()
                if symbol[top_symbol] != i:
                    return False
    return len(stack) == 0


if __name__ == '__main__':
    assert symbol_balance("]") == False
    assert symbol_balance("()[}") == False
    assert symbol_balance("()[]") == True
    assert symbol_balance("([])[]") == True
    assert symbol_balance("([{}])[]") == True
    assert symbol_balance("([{}])[}]") == False
    assert symbol_balance("([{{}])[}]") == False
    assert symbol_balance("(([{}])[{()}]))") == False
    assert symbol_balance("((([{}])[{()}]))") == True