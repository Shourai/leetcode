class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [x.lower() for x in s if x.isalnum()]
        return arr == arr[::-1]

s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "

print(Solution().isPalindrome(s))
