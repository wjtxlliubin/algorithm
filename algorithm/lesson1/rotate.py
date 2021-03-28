class Solution:
    def rotate(self, nums, k) -> None:
        n = len(nums)
        k %= n
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(0, n - k - 1)
        reverse(n - k, n - 1)
        reverse(0, n - 1)
        return nums
if __name__ == '__main__':
    result = Solution().rotate([1,2,3,4,5,6,7],1)
    print(result)
