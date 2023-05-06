class Stack:
    def __init__(self, maxSize):
        self.items = []
        self.maxSize = maxSize

    def isFull(self):
        if len(self.items) == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.items == 0:
            return True
        else:
            return False

    def Push(self, item):
        """
        :param item: this function is used to push items in stack
        :return:
        """
        if len(self.items) < self.maxSize:
            self.items.append(item)
        else:
            return "Stack is Full You can't Update any Items!!"

    def Pop(self):
        """
        :return: it returns the last element which is popped from stack
        """
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return "Stack is Empty!!"

    def topOfStack(self):
        if (len(self.items)) != 0:
            return self.items[len(self.items) - 1]
        else:
            return "Stack is Empty!!"

    def displayStack(self):
        if len(self.items) != 0:
            return self.items
        else:
            return "Stack is Empty!!"


stack = Stack(5)
print(stack.displayStack())
print(stack.Push(1))
print(stack.displayStack())
print(stack.Push(2))
print(stack.displayStack())
print(stack.topOfStack())
print(stack.isEmpty())
print(stack.Pop())
print(stack.displayStack())
print(stack.isFull())
print(stack.Push(1))
print(stack.Push(2))
print(stack.Push(3))
print(stack.Push(4))
print(stack.Push(5))
print(help(Stack))
print(dir(Stack))
