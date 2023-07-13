class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        i = 0
        j = len(height)-1

        while(i<j):
            minimum = min(height[i], height[j])
            temp = minimum * (j-i)
            if temp >max :
                max = temp
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max