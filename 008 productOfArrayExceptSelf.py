class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            leftProduct = []
            rightProduct = nums.copy()
            length = len(nums)
            result = []
            for i in range(length):
                if i==0:
                    leftProduct.append(1)
                else:
                    leftProduct.append(leftProduct[i-1]*nums[i-1])

            for i in range(1, length+1):
                if i == 1:
                    rightProduct[-i]=1
                else:
                    rightProduct[-i]= rightProduct[-i+1]*nums[-i+1]


            # print(leftProduct)
            # print(rightProduct)
            for i in range(length):
                if i == 0:
                    result.append(rightProduct[0])
                elif i == length-1:
                    result.append(leftProduct[-1])
                else:
                    result.append(leftProduct[i]* rightProduct[i]) 
            return result