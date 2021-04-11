#350. 两个数组的交集 II
class Solution:
    def intersect(self, nums1, nums2):

        nums1_dict = {}
        for i in nums1:
            if nums1_dict.get(i):
                nums1_dict[i]+=1
            else:
                nums1_dict[i]=1
        result=[]
        for i in nums2:
            if nums1_dict.get(i) and nums1_dict.get(i)>0:
                nums1_dict[i] = nums1_dict.get(i)-1
                result.append(i)
        return result




if __name__ == '__main__':
    result = Solution().intersect([1,2,2,1],[2,2])
    print(result)