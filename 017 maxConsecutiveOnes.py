class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        ans = 0
        zero = 0

        while(j<len(nums)):
            if nums[j]==0:
                zero +=1 
            while(zero>k):
                if nums[i]==0:
                    zero -=1
                i+=1
            j+=1
            ans = max(ans,j-i)
        print(ans)
        return ans