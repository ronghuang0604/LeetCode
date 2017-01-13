class Solution(object):
    def fizzBuzz(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = []
        for i in range(1, num+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 5 == 0:
                result.append("Buzz")
            elif i % 3 == 0:
                result.append("Fizz")
            else:
                result.append(str(i))
        return result

if __name__ ==  "__main__":
    print(Solution().fizzBuzz(15))
