class Solution(object):
# 注意，这道题array 里面的elements 是从1 开始，
# 如果每个value-1 就会得到所有的indexes。如果是好的array的话， value：1-8, indexes will be 0-7
# 那如果是不好的array的话[4,3,2,7,8,2,3,1]， indexes will be 3,2,1,6,7,1,2,0 找出本应该出现的value 体现在本应该出现的index， value 是对应的 index-1

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result

if __name__ == "__main__":
    print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
