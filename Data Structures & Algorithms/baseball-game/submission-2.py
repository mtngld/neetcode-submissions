class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for x in operations:
            print(stack)
            try:
                stack.append(int(x))
            except:
                pass
            if x == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a)
                stack.append(b)
                stack.append(a + b)
            if x == "C":
                stack.pop()
            if x == "D":
                a = stack.pop()
                stack.append(a)
                stack.append(2*a)
        
        s = 0
        while stack:
            s += stack.pop()
        return s
