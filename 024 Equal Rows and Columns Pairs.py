# he following solution has the time complexity of O(n^2)
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count =0
        columns = {}
        for j in range(len(grid)):
            res = []
            for i in range(len(grid)):
                res.append(grid[i][j])
            columns[j] = res
        for i in range(0,len(grid)):
            temp = grid[:][i]
            for key in columns:
                if columns[key]== temp:
                    count +=1
        return count