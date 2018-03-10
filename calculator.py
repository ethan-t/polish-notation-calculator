from stacks import Stack

def is_number(x):
    "Basic function to check if number is valid for the operations"
    try:
        float(x)
        return True
    except:
        return False

def evaluate(operator, x, y):
    "Evaluates a expression given a operation and two inputs"
    x = float(x)
    y = float(y)
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y

def calc(expr):
    "Processes an expression written in Polish notation from left to right"
    # Create Stack objects for the operators and operands
    operatorStack = Stack()
    operandStack = Stack()
    # Split expression into a list (temporary)
    expr = expr.split()
    for token in expr:
        # Check if the token is an operator
        if token in ["+", "-", "*", "/"]:
            print("Found operator " + token)
            operatorStack.push(token)
            pendingOperand = False
        # Check if the operand is a valid number
        elif is_number(token):
            print("Found operand " + token)
            operand = token
            if pendingOperand == True:
                while operandStack.height() != 0:
                    operand_1 = operandStack.pop()
                    operator = operatorStack.pop()
                    print("Evaluating " + str(operand_1) + " " + operator + " " + str(operand))
                    operand = evaluate(operator, operand_1, operand)
                    print("Evaluation returned " + str(operand))
            operandStack.push(operand)
            pendingOperand = True
        print("The items of the operandStack read: " + str(operandStack.items))
        print("The items of the operatorStack read: " + str(operatorStack.items))
    return operandStack.pop()

print(calc("- * / 15 - 7 + 1 1 3 + 2 + 1 1"))
