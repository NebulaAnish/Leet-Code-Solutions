# Solution by using Sliding Windows Technique

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k
        sum = 0
        result = 0
        if len(nums) == 1:
            return max(nums)
        for f in range(k):
            sum += nums[f]
        result = sum
        while (j<=len(nums)-1):
            i +=1
            j +=1
            
            temp = sum - nums[i-1] + nums[j-1]
            sum = temp
            if temp > result:
                result = temp
        return result/k