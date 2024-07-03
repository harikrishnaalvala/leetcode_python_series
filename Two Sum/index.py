class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        M = {}
        for i in range(n):
            x = target - nums[i]
            if nums[i] in M:
                return [M[nums[i]],i]
            else:
                M[x] = i
