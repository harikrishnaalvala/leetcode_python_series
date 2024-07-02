class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, curr_sum = 0,0,nums[0]
        res = float('inf')

        while True:
            if curr_sum >= target:
                res = min(res, r-l+1)
                curr_sum -= nums[l]
                l += 1
            else:
                r += 1
                if r >= len(nums):
                    break
                curr_sum += nums[r]
        
        return res if res != float('inf') else 0
