class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       return reduce(lambda r,q:r[:-1]+[[r[-1][0],max(r[-1][1],q[1])]] if r and r[-1][1]>=q[0] else r+[q],sorted(intervals+[newInterval]),[])
