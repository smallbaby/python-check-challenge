# -*- coding: utf-8 -*-
# Author: kaizhang01


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        j = 0
        while j <= len(haystack) - len(needle):
            if haystack[j:len(needle)+j] == needle:
                return j
            else:
                j += 1
        return -1


if __name__ == '__main__':
    print(Solution().strStr("a", "a"))
