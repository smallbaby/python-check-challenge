# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2019/1/10
# Desc: 一个数在集合中的个数超过一半


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        maxNum = 0
        cnt = 1
        if len(numbers) == 0:
            return maxNum
        maxNum = numbers[0]
        if len(numbers) < 2:
            return numbers[0]
        for j in range(1, len(numbers)):
            i = numbers[j]
            if i == maxNum:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    cnt = 1
                    maxNum = i
        total = 0
        for i in numbers:
            if i == maxNum:
                total += 1
        if total * 2 <= len(numbers):
            return 0
        return maxNum


k = Solution().MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2])
print(k)
