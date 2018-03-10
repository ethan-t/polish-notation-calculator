from stacks import Stack

def is_number(x):
    try:
        float(x)
        return True
    except:
        return False

def calc(expr):
    stack = Stack()
    expr = expr.split()
    for token in expr:
        if token in ["+", "-", "*", "/"]:
            print("Found operator " + token)
        elif is_number(token):
            print("Found operand " + token)

calc("* 2 4")
