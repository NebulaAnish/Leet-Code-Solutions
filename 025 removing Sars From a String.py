
# O(N) solution timewise and both space wise.

def removeStars1(s):
    result = []
    for i in s:
        result.append(i)
        if i=='*':
            result.pop()
            result.pop()
    return ''.join(result)

# It's time complexity is O(N) and space complexity is constant i.e O(1).
def removeStars2(s):
    result = ""
    for i in s:
        result +=i
        if i=='*':
            result = result[:-2]
    return result