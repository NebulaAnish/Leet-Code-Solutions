class Solution:
    def swap(self, a,b):
        temp = a
        a = b
        b = temp
        return a, b

    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        minIndex = min(l1, l2)
        maxIndex = max(l1,l2)
        # Determine the longer word
        longerWord = word1
        if (l2>l1):
            longerWord = word2
        
        # Append to the temp string alternatively upto minIndex
        temp = ''
        for i in range(minIndex):
            temp = temp + word1[i] + word2[i]
        
        # Append remaining letters in the longerWord at the end
        temp += longerWord[minIndex:]
        return temp