class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            n_dash = n & 1
            if n_dash == 1:
                count += 1
            n = n >> 1

        return count
        
