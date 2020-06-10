class MaxStack:
    def __init__(self):
        self.stack=[]
        self.cur_max=float('-inf')

    def push(self, val):
        self.stack.append(val)
        if val>self.cur_max:
            self.cur_max=val
        self.stack.append(self.cur_max)

    def pop(self):
        self.stack.pop()
        self.stack.pop()

    def max(self):
        return self.stack[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
