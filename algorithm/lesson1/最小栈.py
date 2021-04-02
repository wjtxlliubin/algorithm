class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self) :
        if self.stack:
            self.stack = self.stack[:-1]

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self) :
        return min(self.stack) if self.stack else None

if __name__ == '__main__':
    result = MinStack()

    result.pop()
    print(result.top())
    print(result.getMin())