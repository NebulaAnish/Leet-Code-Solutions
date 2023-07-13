class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)== 1:
            return
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

# O(N) solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l==1 or l==0 :
            return
        left =0
        right = 0
        while(right<l):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right +=1
            
            else:
                right +=1
        return