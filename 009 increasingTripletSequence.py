class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        low = max(nums)+1
        mid = low

        for i in nums:
            if i<low:
                low = i
            if i>low and i<mid:
                mid = i
            if i>mid:
                return True
        return False