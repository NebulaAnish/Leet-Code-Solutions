class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1: 
            print(chars)
            return 1
        chars.append("888")
        result = ""
        count = 0
        temp = chars[0]
        for i in range(len(chars)):
            if temp == chars[i]:
                count +=1
            else:
                result += chars[i-1]
                if count !=1:
                    result += str(count)
                # resultCount +=  
                temp = chars[i]
                count = 1

        chars.clear()
        chars.extend(result)
        # print(chars)
        return len(chars)