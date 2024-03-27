class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        d1 = {}
        d2 = {}
        for ch in s1:
            if ch not in d1:
                d1[ch] = 1
            else:
                d1[ch] += 1

        left = 0
        right = 0

        for i in range(len(s2)):
            if s2[i] in d1:
                left = i
                right = left + len(s1)
                if right > len(s2):
                    return False
                for j in range(left, right):
                    if s2[j] not in d2:
                        d2[s2[j]] = 1
                    else:
                        d2[s2[j]] += 1
                if d1 == d2:
                    return True
                else:
                    d2 = {}

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
    # case_one()
    # case_two()
    # case_three()
    # case_four()
    case_five()
