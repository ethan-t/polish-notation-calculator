# Polish Notation Calculator

A calculator, written in Python, that evaluates mathematical expressions written in Polish notation. It implements the following algorithm that processes the expression left to right, taken from [Wikipedia](https://en.wikipedia.org/wiki/Polish_notation#Prefix_evaluation_algorithm):

```
for each token in the prefix expression:
  if token is an operator:
    push token onto the operator stack
    pending_operand ← False
  else if token is an operand:
    operand ← token
    if pending_operand is True:
      while the operand stack is not empty:
        operand_1 ← pop from the operand stack
        operator ← pop from the operator stack
        operand ← evaluate operator with operand_1 and operand
    push operand onto the operand stack
    pending_operand ← True
result ← pop from the operand stack
```
## Stack

This was essentially created to use the Stack implementation from my [algorithms repository](https://github.com/ethan-t/algorithms).

## Todo (maybe)

- Support for parentheses
- More operations 
