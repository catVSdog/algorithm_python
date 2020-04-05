def replace_blank_a(origin, target):
    """
    替换空格为指定字符
    复杂度 O(n)
    """
    new_string = ''
    for i in origin:
        if i == ' ':
            new_string += target
        else:
            new_string += i
    return new_string


def replace_blank_b(origin, target):
    return ''.join([i if i != ' ' else target for i in origin])


if __name__ == '__main__':
    a = 'we are winer'
    print(replace_blank_b(a, '%20'))
