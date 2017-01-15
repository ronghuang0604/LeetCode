class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result = result ^ i
        return result

if __name__ == "__main__":
    print(Solution().singleNumber([2,1,3,5,6,3,5,1,2,6,25]))
