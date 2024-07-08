class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for x in range(0,len(nums)):
            if nums[x]==target:
                return x
        return -1
        
