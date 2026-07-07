class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            print(f"{c=}, {s=}, {stack=}")
            if c in ["(", "{", "["]:
                stack.append(c)
            elif c in [")", "}", "]"]:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if c == ")" and last != "(":
                    return False
                if c == "}" and last != "{":
                    return False
                if c == "]" and last != "[":
                    return False
        if len(stack) > 0:
            return False
        return True
        