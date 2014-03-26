
operators = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '-': lambda a, b: a - b,
    '^': lambda a, b: a ** b,
}


def evaluate_postfix(expr, debug=False):
    """
    this evaluates iterables containing numbers and arithmetic operators
    as postfix arithmetic expressions
    >>> evaluate_postfix([1, 2, '+'])
    3
    >>> evaluate_postfix([3, 2, '*'])
    6
    >>> evaluate_postfix([10, 3, 7, '+', '*', 3, '+'])
    103
    """
    number_stack = []

    for e in expr:
        if e in operators:
            op = operators[e]
            a = number_stack.pop()
            b = number_stack.pop()
            res = op(a, b)
            if debug:
                print "{0} {1} {2} = {3}".format(a, e, b, res)
            number_stack.append(res)
        else:
            number_stack.append(e)

    return number_stack[0]
