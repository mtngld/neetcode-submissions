class MinStack:

    def __init__(self):
        self.data = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min_vals or val < self.min_vals[-1]:
            self.min_vals.append(val)
        else:
            self.min_vals.append(self.min_vals[-1])
        

    def pop(self) -> None:
        self.data.pop()
        self.min_vals.pop()
        

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]
        
