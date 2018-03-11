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
            operatorStack.push(token)
            pendingOperand = False
        # Check if the operand is a valid number
        elif is_number(token):
            operand = token
            # Check if a calculation should be done
            if pendingOperand == True:
                while operandStack.height() != 0:
                    operand_1 = operandStack.pop()
                    operator = operatorStack.pop()
                    # print("Evaluating " + str(operand_1) + " " + operator + " " + str(operand))
                    operand = evaluate(operator, operand_1, operand
            # Push the number to the operand stack
            operandStack.push(operand)
            pendingOperand = True
    # Return result
    return operandStack.pop()

if __name__ == "__main__":
    # Read-Eval-Print Loop
    while True:
        expr = raw_input("> ")
        print(calc(expr))
