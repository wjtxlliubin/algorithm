class Solution:
    def threeSum(self, nums):
        if (not nums or len(nums) < 3):
            return []
        nums = sorted(nums)
        result = []
        for index in range(len(nums) - 1):
            if (nums[index] > 0):
                return result
            if (index > 0 and nums[index] == nums[index - 1]):
                continue
            first = index + 1
            last = len(nums) - 1
            while first < last:
                if nums[index] + nums[first] + nums[last] == 0:
                    result.append([nums[index], nums[first], nums[last]])
                    while (first < last and nums[first] == nums[first + 1]):
                        first += 1
                    while (first < last and nums[last] == nums[last - 1]):
                        last -= 1
                    first += 1
                    last -= 1
                elif nums[index] + nums[first] + nums[last] > 0:
                    last -= 1
                else:
                    first += 1
        return result


if __name__ == '__main__':
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print(result)
