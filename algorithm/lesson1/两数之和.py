class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [hashmap.get(target - num), i]
            hashmap[num] = i


if __name__ == '__main__':
    result = Solution().twoSum([3, 3], 6)
    print(result)
