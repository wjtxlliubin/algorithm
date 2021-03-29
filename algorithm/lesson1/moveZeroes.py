class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        key =0

        while i < len(nums) and key < len(nums):
            if nums[i] != 0:
                nums[key], nums[i] = nums[i], nums[key]
                key += 1
            i += 1

        return  nums


if __name__ == '__main__':
    result = Solution().moveZeroes([0,1,0,3,12])
    print(result)