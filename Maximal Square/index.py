class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        
        # ans to store the max length of square found
        ans = 0
        
        # dp of size row + 1 and col + 1
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        
        # start from the bottom of the original list
        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                
                # if in original matrix (r,c) is 0 then dp[r][c] = 0
                if matrix[r][c] == '0':
                    dp[r][c] = 0
                
                # else dp[r][c] = original[r][c] + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
                
                # update the ans to maximum length of square found
                ans = max(ans, dp[r][c])
                
        # once maximum length is found return the square of length
        return ans ** 2
