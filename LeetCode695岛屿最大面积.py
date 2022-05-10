# 公司 步微科技
# 编写人    ponybeep
# 开发时间：2022-5-11 5:06
import collections


# 方法一 深度优先（使用栈）
class Solution1:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxnum,m,n = 0,len(grid),len(grid[0])
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    grid[i][j] = 0
                    num =0
                    while stack:
                        x,y = stack.pop()
                        num+=1
                        for mx,my in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                            if 0 <=mx < m and 0 <=my < n and grid[mx][my] == 1:
                                stack.append((mx,my))
                                grid[mx][my] = 0
                    maxnum = max(maxnum,num)
        return maxnum

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
solution1 = Solution1()
print('测试方法一：答案是6就对了！')
print(solution1.maxAreaOfIsland(grid))


# 方法二
class Solution2:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxnum,m,n = 0,len(grid),len(grid[0])
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if grid[i][j] == 1:
                    deq = collections.deque([(i,j)])
                    grid[i][j] = 0
                    num =0
                    while deq:
                        x,y = deq.popleft()
                        num+=1
                        for mx,my in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                            if 0 <=mx < m and 0 <=my < n and grid[mx][my] == 1:
                                deq.append((mx,my))
                                grid[mx][my] = 0
                    maxnum = max(maxnum,num)
        return maxnum


solution2 = Solution2()
print('测试方法二：答案是6就对了！')
print(solution2.maxAreaOfIsland(grid))

