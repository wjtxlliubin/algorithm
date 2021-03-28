class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 :
            return nums2
        if n == 0 :
            return nums1
        next1 = next2 =  0
        result = []
        while next1 < m and next2 < n:
            if nums1[next1]>nums2[next2]:
                result.append(nums2[next2])
                next2 += 1
            else:
                result.append(nums1[next1])
                next1 += 1
        if next1 == m :
            result.extend(nums2[next2:])
        else:
            result.extend(nums2[next1:])
        return result

if __name__ == '__main__':
    result = Solution().merge([1,2],2,[2,5],2)
    print(result)