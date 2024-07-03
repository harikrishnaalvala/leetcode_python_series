class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result, q = 0, -inf
        for s, e in sorted(points):
            result += q < s
            q = e if q < s else min(q, e)

        return result
