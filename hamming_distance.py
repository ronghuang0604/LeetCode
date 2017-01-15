class Solution(object):
    def hammingDistance(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # easy version
        return bin(num1 ^ num2).count("1")


if __name__ == "__main__":
    print(Solution().hammingDistance(3,8))
