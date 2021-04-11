#面试题59 - I. 滑动窗口的最大值
class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        if not nums:
            return []
        for i in range(k - 1, len(nums)):
            result.append(max(nums[i - k + 1:i + 1]))
        return result


import collections
class Solution1:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0: return []
        deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res

if __name__ == '__main__':
    result = Solution1().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
    print(result)