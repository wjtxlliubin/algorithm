#412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n):
        list_str = []
        for i in range(1,n+1):
            if i %3 ==0 and i%5==0:
                input_str = "FizzBuzz"
            elif i % 3 == 0:
                input_str = "Fizz"
            elif i%5==0:
                input_str = "Buzz"
            else:
                input_str = str(i)
            list_str.append(input_str)
        return list_str
if __name__ == '__main__':
    result = Solution().fizzBuzz(15)
    print(result)
