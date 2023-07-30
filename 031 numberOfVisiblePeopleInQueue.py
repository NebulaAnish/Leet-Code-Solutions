class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        A = heights
        res = [0] * len(A)
        stack = []
        for i, v in enumerate(A):
            while stack and A[stack[-1]] <= v:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res