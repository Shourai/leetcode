from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        default_dict = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            default_dict[key].append(str)
        return list(default_dict.values())

def case_one():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))
    assert(Solution().groupAnagrams(strs)) == [["bat"],["nat","tan"],["ate","eat","tea"]]


def case_two():
    strs = [""]
    assert(Solution().groupAnagrams(strs)) == [[""]]


def case_three():
    strs = ["a"]
    assert(Solution().groupAnagrams(strs)) == [["a"]]


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
