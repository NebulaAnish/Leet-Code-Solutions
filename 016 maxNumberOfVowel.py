class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s=s.upper()
        i = 0
        j = k
        count = 0
        vowels = 'AEIOU'
        # vowel count of first k-length sub string
        for t in s[i:k]:
            if t in vowels:
                count +=1
        # assume first count is the maximum
        maxVowel = count

        # slide the window upto the end of the string
        while (j<len(s)):
            # subtract 1 if exiting element is vowel
            if s[i] in vowels:
                count -= 1
            i+=1
            j+=1
            # add 1 if entering element is vowel
            if s[j-1] in vowels:
                count +=1
            # replace maxVowel if greater number of vowels is found
            if count >= maxVowel:
                maxVowel = count
        return maxVowel