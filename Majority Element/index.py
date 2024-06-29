class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        d=n//2
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for i in c:
            if c[i]>d:
                return i
