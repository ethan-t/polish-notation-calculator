# A stack is a data structure that is like a
# physical stack: items added most recently added
# to the top will be removed first.
#
# This implementation has four methods:
# - Push, to add to the top of the stack
# - Pop, to remove from the item from the top of the stack
#   and return the result
# - Peek, to return the top item without removing it
# - Clear, to remove every item from the stack


class Stack():

    def __init__(self):
        self.items = []

    def push(self, object):
        self.items.append(object)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def clear(self):
        self.items = []

    def height(self):
        return len(self.items)
