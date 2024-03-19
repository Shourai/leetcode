class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = []
        max_len_substr = 0
        for ch in s:
            if ch not in substr:
                substr.append(ch)
                if len(substr) > max_len_substr:
                    max_len_substr = len(substr)
            else:
                substr = substr[substr.index(ch)+1::]
                substr.append(ch)
        return max_len_substr


def case_one():
    s = "abcabcbb"
    assert (Solution().lengthOfLongestSubstring(s)) == 3


def case_two():
    s = "bbbbb"
    assert (Solution().lengthOfLongestSubstring(s)) == 1


def case_three():
    s = "pwwkew"
    assert (Solution().lengthOfLongestSubstring(s)) == 3


def case_four():
    s = " "
    assert (Solution().lengthOfLongestSubstring(s)) == 1


def case_five():
    s = "dvdf"
    assert (Solution().lengthOfLongestSubstring(s)) == 3


def case_six():
    s = "ohvhjdml"
    assert (Solution().lengthOfLongestSubstring(s)) == 6

if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
    case_four()
    case_five()
    case_six()
