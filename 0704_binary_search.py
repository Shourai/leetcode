class Solution:
    def search(self, nums: list[int], target: int) -> int:
        output = -1
        if target in nums:
            output = nums.index(target)
        return output

        
def case_one():
    nums = [-1,0,3,5,9,12]
    target = 9
    output = 4
    assert(Solution().search(nums, target)) == output


def case_two():
    nums = [-1,0,3,5,9,12]
    target = 2
    output = -1
    assert(Solution().search(nums, target)) == output


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
