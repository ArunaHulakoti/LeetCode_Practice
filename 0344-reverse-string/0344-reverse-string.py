from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

s = ["A", "m", "a", "n"]
sol = Solution()
sol.reverseString(s)  # This modifies s in-place
print(s)  # Output: ['n', 'a', 'm', 'A']
