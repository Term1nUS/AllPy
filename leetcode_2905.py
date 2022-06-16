class Solution:
    def maxProduct(self, words: list[str]) -> int:
        wrds = words
        maxprod = 0
        for i in range(0, len(wrds) - 1):
            for j in range(i+1, len(wrds)):
                hascross = False
                for ltr in list(wrds[i]):
                    if wrds[j].find(ltr) >= 0:
                        hascross = True
                        break
                if not hascross:
                    currprod = len(wrds[i])*len(wrds[j])
                    if currprod > maxprod:
                        maxprod = currprod
                hascross = False
        return maxprod



s = Solution()
print(s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(s.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(s.maxProduct(["a", "aa", "aaa", "aaaa"]))
