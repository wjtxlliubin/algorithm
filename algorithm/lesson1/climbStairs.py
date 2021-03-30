class Solution:
    def climbStairs(self, n):
        f = 1
        s = 2
        if n == 1 :
            return 1
        if n == 2 :
            return 1
        while n-2>0:
            f ,s = s,f+s
            n-=1
        return s

if __name__ == '__main__':
    result = Solution().climbStairs(4)
    print(result)
