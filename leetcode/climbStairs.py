# -*- coding: utf-8 -*-
# Author: kaizhang01


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    x = Solution().climbStairs(4)
    print(x)


