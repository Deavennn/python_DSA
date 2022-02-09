class Stack:
    def __init__(self):
        self.stack = []
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def remove(self):
        if len(self.stack) <= 0:
            return 'stack empty'
        else:
            return self.stack.pop()

stk = Stack()
for i in range(1,11):
    stk.add(i)
for i in stk.stack:
    print(i)
stk.remove()
for i in stk.stack:
    print(i)
