class Solution(object):
    # The fist thing came to my mind was to convert the num to bit string using bin(num)
    # However, using left shift is a great way to create a mask, and mask ^ num
    # 注意，因为mask永远都是1,2,4,8,16 。。。 的增长，mask-1 就正好得到跟num一样长的都是1的bit string.

    def numComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 1
        while mask <= num:
            mask = mask << 1
        mask = mask -1
        return num ^ mask

if __name__ == "__main__":
    print(Solution().numComplement(9))
    print(Solution().numComplement(8))
