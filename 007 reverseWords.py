class Solution:
    def reverseWords(self, s: str) -> str:
				#Remove any leading or trailing spaces
        s = s.strip()
        length = len(s)
        findSpace = True
        result = []
        tempIndex  = length
        i = length
				# Loop i from behind and concat each word to result
        while i>=0:
            i-=1
            if findSpace:
                if s[i]==" ":
                    result.append(s[i+1:tempIndex])
                    # print(i+1)
                    # print(tempIndex)
                    findSpace = False
            elif not findSpace:
                if s[i] != " ":
                    findSpace = True
                    tempIndex = i+1
        result.append(s[i+1:tempIndex])
				# Convert result from list to string 
        result = " ".join(result)
        return result

## SOlution 2
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = s[::-1]
        res = ""
        s = [x if x!="" and x!=" " else None for x in s ]
        while None in s:
            s.remove(None)
        s= " ".join(s)
        
        return s