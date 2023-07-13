class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)
        vowel = "aeiouAEIOU"
        s = list(s)

        while (i<j):
            if s[i] in vowel:
                while(j>i):
                    j-=1
                    if s[j] in vowel:
                        s[i], s[j] = s[j], s[i]
                        break
            i+=1
        s = "".join(s)
        return s