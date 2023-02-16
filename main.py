class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i, v in enumerate(x):
            if v != x[len(x)-i-1]:
                return False
        return True