class Solution(object):
    # xor finds sum without carry
    # and finds all the CARRY, but you need to shift it to the left for one place just like what you do in math
    # then add the carry to the xor result, but since this is addition, you can just use recursion and set a = carry_without_carry, b = carry 

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
