class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSum, maxSum = 0, -sys.maxsize
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        
        currSum = 0
        max2 = 0
        for i in range(len(nums)):
            maxSum = max(maxSum, sums+max2)
            sums -= nums[i]
            currSum += nums[i]
            max2 = max(max2, currSum)
        
        return maxSum
