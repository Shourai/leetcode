from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        counter = Counter(s1)
        matched = 0

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
                if counter[s2[i]] == 0:
                    matched += 1

            if i >= n and s2[i-n] in counter:
                if counter[s2[i-n]] == 0:
                    matched -= 1
                counter[s2[i-n]] += 1

            if matched == len(counter):
                return True
        return False


def case_one():
    s1 = "ab"
    s2 = "eidbaooo"
    assert Solution().checkInclusion(s1, s2) is True


def case_two():
    s1 = "ab"
    s2 = "eidboaoo"
    assert Solution().checkInclusion(s1, s2) is False


def case_three():
    s1 = "adc"
    s2 = "dcda"
    assert Solution().checkInclusion(s1, s2) is True

def case_four():
    s1 = "hello"
    s2 = "ooolleoooleh"
    assert Solution().checkInclusion(s1, s2) is False

def case_five():
    s1 = "ccc"
    s2 = "cbac"
    assert Solution().checkInclusion(s1, s2) is False

if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
    case_four()
    case_five()
