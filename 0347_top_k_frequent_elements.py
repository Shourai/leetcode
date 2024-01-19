from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        sorted_list = sorted(count.items(), key=lambda x: x[1], reverse=True)
        frequent_list = [i[0] for i in sorted_list][0:k]
        return frequent_list


def case_one():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert (Solution().topKFrequent(nums, k)) == [1, 2]


def case_two():
    nums = [1]
    k = 1
    assert (Solution().topKFrequent(nums, k)) == [1]


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
