# 公司 步微科技
# 编写人    ponybeep
# 开发时间：2022-5-8 9:28

def floodFill(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
    if newColor == image[sr][sc]:
        return image
    stack, old = [(sr, sc)], image[sr][sc]
    while stack:
        point = stack.pop()
        image[point[0]][point[1]] = newColor
        for new_i, new_j in zip((point[0], point[0], point[0] + 1, point[0] - 1), (point[1] + 1, point[1] - 1, point[1], point[1])):
            if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == old:
                stack.append((new_i, new_j))
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc = 1, 1
new_color = 2
image = floodFill(image, sr, sc, new_color)
print(image)


# class Solution:
#     def floodFill(self, image: List[list[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         if image[sr][sc] == newColor:
#             return image
#         stack, currColor = [(sr, sc)], image[sr][sc]
#         while stack:
#             point = stack.pop()
#             image[point[0]][point[1]] = newColor
#             for dx, dy in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1),
#                            (point[0], point[1] + 1)]:
#                 # for dx, dy in [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)]:
#
#                 if 0 <= dx < len(image) and 0 <= dy < len(image[0]) and image[dx][dy] == currColor:
#                     stack.append((dx, dy))
#         return image