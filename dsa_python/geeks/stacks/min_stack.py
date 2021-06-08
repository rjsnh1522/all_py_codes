class MinStack:
    def __init__(self):
        self.stk = []
        self.min_stack = []
        self.stack_top = None
        self.min_stack_top = None

    def push(self, val):
        self.stk.append(val)
        if self.min_stack_top is None:
            self.min_stack.append(val)
        else:
            curr_min = self.min_stack[self.min_stack_top]
            if val < curr_min:
                self.min_stack.append(val)
        self.set_top_of_stack()

    def pop(self):
        if self.stack_top is None:
            pass
        else:
            val = self.stk.pop(-1)
            if val == self.min_stack[self.min_stack_top]:
                self.min_stack.pop(-1)
        self.set_top_of_stack()

    def set_top_of_stack(self):
        self.stack_top = len(self.stk) - 1 if len(self.stk) > 0 else None
        self.min_stack_top = len(self.min_stack) - 1 if len(self.min_stack) > 0 else None

    def top(self):
        if self.stack_top is None:
            return -1
        else:
            return self.stk[self.stack_top]

    def getMin(self):
        if self.min_stack_top is None:
            return -1
        else:
            return self.min_stack[self.min_stack_top]



st = MinStack()
st.push(10)
st.push(9)
print("get_min 1", st.getMin())
st.push(8)
print("get_min 2", st.getMin())
st.push(7)
print("get_min 3", st.getMin())
st.push(6)
print("get_min 4", st.getMin())
st.pop()
print("get_min 5", st.getMin())
st.pop()
print("get_min 6", st.getMin())
st.pop()
print("get_min 7", st.getMin())
st.pop()
print("get_min 8", st.getMin())
st.pop()
print("get_min 9", st.getMin())
