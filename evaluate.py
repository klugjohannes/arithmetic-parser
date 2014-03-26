op_queue = []
number_stack = []

operators = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '-': lambda a, b: a - b,
    '^': lambda a, b: a ** b,
}


def evaluate_postfix(expr):
    for e in expr:
        if e in operators:
            op = operators[e]
            a = number_stack.pop()
            b = number_stack.pop()
            res = op(a, b)
            print "{0} {1} {2} = {3}".format(a, e, b, res)
            number_stack.append(res)
        else:
            number_stack.append(e)

    print number_stack[0]

postorder = [9.9, 3.4, 7, '+', '*', 3, '+']

evaluate_postfix(postorder)
