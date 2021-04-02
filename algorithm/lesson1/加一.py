class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] is not 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if digits[0] is 0:
                    digits.insert(0, 1)
                    return digits


if __name__ == '__main__':
    result = Solution().plusOne([9, 9])
    print(result)
