#https://leetcode-cn.com/problems/bulls-and-cows/
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_l = [[] for _ in range(10)]
        guess_l = [[] for _ in range(10)]
        for i in range(len(secret)):
            secret_l[int(secret[i])].append(i)
        for i in range(len(guess)):
            guess_l[int(guess[i])].append(i)

        lenth = len(secret)

        def same_word_num(nums1, nums2):
            l = [0] * lenth
            for num in nums1:
                l[num] += 1
            for num in nums2:
                l[num] += 1
            result = 0

            for num in l:
                if num == 2:
                    result += 1
            return result

        total_same = 0
        total_diff = 0
        for i in range(10):
            if guess_l[i] and guess_l[i]:
                num = same_word_num(secret_l[i], guess_l[i])
                total_same += num
                total_diff += min(len(secret_l[i]), len(guess_l[i])) - num

        return '%d' % total_same + 'A' + '%d' % (total_diff) + 'B'