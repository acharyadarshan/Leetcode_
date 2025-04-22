class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
         memo = {}
         def uq(k,l): 
            if k>=m or l>=n: 
                return 0 
            if k == m-1 and l == n-1: 
                return 1
            if (k,l) in memo: 
                return memo[(k,l)]
            memo[(k,l)] = uq(k+1,l) + uq(k,l+1)
            return memo[(k,l)]

         return uq(0,0)
    
    ##
    # class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:

    #     dp = [[1]* (n) for _ in range(m)]
    #     #base cases 
    #     for i in range(1,m): 
    #         for j in range(1,n):
    #             dp[i][j] = dp[i][j-1] + dp[i-1][j]
          
    #     return dp[m-1][n-1]

    