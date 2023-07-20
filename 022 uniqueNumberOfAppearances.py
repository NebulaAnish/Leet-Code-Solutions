class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countOfOccurences = {}
        for arrayElement in arr:
            countOfOccurences[arrayElement]=0

        for arrayElement in arr:
            if arrayElement in countOfOccurences:
                countOfOccurences[arrayElement]+=1

        arrayOfCounts = [countOfOccurences[x] for x in countOfOccurences]
        setOfCounts = set(arrayOfCounts)
        return len(arrayOfCounts)==len(setOfCounts)