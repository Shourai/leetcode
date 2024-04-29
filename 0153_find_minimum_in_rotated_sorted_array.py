class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


def case_one():
    nums = [3, 4, 5, 1, 2]
    output = 1
    assert Solution().findMin(nums) == output


def case_two():
    nums = [4,5,6,7,0,1,2]
    output = 0
    assert Solution().findMin(nums) == output


def case_three():
    nums = [11,13,15,17]
    output = 11
    assert Solution().findMin(nums) == output


def case_four():
    nums = [2,3,4,5,1]
    output = 1
    assert Solution().findMin(nums) == output

def case_five():
    nums = [1,2]
    output = 1
    assert Solution().findMin(nums) == output

if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
    case_four()
    case_five()
