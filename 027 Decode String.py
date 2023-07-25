class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                substr = ""
                # POP till opening bracket
                while stack[-1] != "[":
                    substr = stack.pop()+substr
                stack.pop()
                # K holds digit(maybe 2/3 digit). 
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop()+k
                
                # Store in stack the latest str multiplied times k
                stack.append(int(k)*substr)
        return "".join(stack)