class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums)-1
        nums.sort()
        count = 0

        while(i<j):
            sum = nums[i] + nums[j]
            if sum == k:
                count +=1
                i+=1
                j-=1
            elif sum>k:
                j-=1
            elif sum<k:
                i+=1
        return count