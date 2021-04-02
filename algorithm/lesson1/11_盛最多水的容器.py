class Solution:
    def maxArea(self, height):
        first, last, maxarea = 0, len(height) - 1, 0

        while first < last:
            if height[first] < height[last]:
                maxarea = max(height[first] * (last - first), maxarea)
                first += 1
            else:
                maxarea = max(height[last] * (last - first), maxarea)
                last -= 1

        return maxarea


if __name__ == '__main__':
    result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
