
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        p = 0
        q = 1
        while (q < len(nums)):
            if nums[p] != nums[q]:
                nums[p + 1] = nums[q]
                p+=1
            q+=1
        return p+1


if __name__ == '__main__':
    result = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(result)