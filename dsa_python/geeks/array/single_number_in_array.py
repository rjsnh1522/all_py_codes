class Solution:
    def singleNumber(self, nums):
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res






s = Solution()
nn = [1,2,3,4,5,1,2,3,4,5,6]
print(s.singleNumber(nn))
