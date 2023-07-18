def findPivotIndex(nums):
    rightSum = 0
    leftSum = 0
    # Find sum of every elements except first
    for i in nums[1:]:
        rightSum +=i
    pivot=0
    # return index if condition is met, else keep increasing pivot from 0 to further
    while(pivot<len(nums)):
        if leftSum == rightSum:
            return pivot
        pivot+=1
        leftSum += nums[pivot-1]
        if pivot!=len(nums):
            rightSum -= nums[pivot] 
    return -1

# Test Cases
if __name__=='__main__':
    a = [2,1,-1]            # 0
    b = [1,7,3,6,5,6]       # 3
    c = [1,2,3]             # -1
    d = [-1,-1,-1,-1,-1,-1] # -1
    e = [-1,-1,0,1,1,0]     # 5
    print("A", findPivotIndex(a))
    print("B", findPivotIndex(b))
    print("C", findPivotIndex(c)) 
    print("D", findPivotIndex(d)) 
    print("E", findPivotIndex(e)) 