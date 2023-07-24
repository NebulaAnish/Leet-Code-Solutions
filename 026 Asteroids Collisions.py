class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        result = []
        for i in asteroids:
            if i>0:
                stack.append(i)
            else:
                while(len(stack))>0 and stack[-1] < abs(i):
                    stack.pop()
                if len(stack)==0:
                    result.append(i)
                elif stack[-1]==abs(i):
                    stack.pop()
        return result+stack
        
