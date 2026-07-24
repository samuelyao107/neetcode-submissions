from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        numIslands = 0
        if grid == []:
            return 0
        
        def DFS(i,j):
            if i<0 or i > len(grid)-1 or j< 0 or j>len(grid[i])-1:
                return
            if grid[i][j]=="1" and (i,j) not in visited:    
                visited.add((i,j))
                DFS(i+1,j)
                DFS(i,j+1)
                DFS(i-1,j)
                DFS(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]== "1" and (i,j) not in visited:
                    numIslands +=1
                    DFS(i,j)
        return numIslands        
