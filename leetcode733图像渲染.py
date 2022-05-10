# 公司 步微科技
# 编写人    ponybeep
# 开发时间：2022-5-7 11:04
class Solution:
    def floodfill(self, image: list[list[int]], sr: int, sc: int, newcolor: int) -> list[list[int]]:
        n, m = len(image), len(image[0])
        currcolor = image[sr][sc]

        def dfs(x: int, y: int):
            if image[x][y] == currcolor:
                image[x][y] = newcolor
                for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < n and 0 <= my < m and image[mx][my] == currcolor:
                        dfs(mx, my)

        if currcolor != newcolor:
            dfs(sr, sc)
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc = 1, 1
new_color = 2
solution = Solution()
solution.floodfill(image, sr, sc, new_color)
print(image)
