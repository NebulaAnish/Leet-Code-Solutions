class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for i in s:
            if i in brackets:
                # If stack is not empty and top value is opening pair of the number
                if stack and stack[-1]==brackets[i]:
                    stack.pop()
                # closing bracket doesn't match with opening bracket
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False