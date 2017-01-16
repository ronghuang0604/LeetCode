class Solution(object):
    def sum_using_xor(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while(b != 0):
            sum_without_carry = a ^ b
            carry = ( a & b ) << 1
            a = sum_without_carry
            b = carry
        return a

if __name__ == "__main__":
    print(Solution().sum_using_xor(13,7))
