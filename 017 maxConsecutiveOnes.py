# This code doesn't pass all the edge cases, Will rework on this problem tomorrow

def func(nums,k):
    i = 0
    j = k
    max = 0
    numOfZero = 0
    for itr in nums[:k]:
        if itr==0:
            numOfZero+=1
    max = 0
    while(j<len(nums) and i<j):
        # print(i,j, numOfZero)
        if numOfZero <=k:
            j+=1
            if nums[j-1]==0:
                numOfZero+=1
            
        if numOfZero >k:
            if nums[i]==0:
                numOfZero-=1
            i+=1
        if (j-i)>max:
            max = j-i
    print(max)
    return max