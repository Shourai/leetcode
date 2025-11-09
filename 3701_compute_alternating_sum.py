class Solution(object):
    def alternatingSum(self, nums:list):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(nums)):
            nums.sort()
            if i%2 == 0:
                total += nums[i]
            else:
                total -= nums[i]
        return total



def case_one():
    nums=[1,3,5,7]
    print(Solution().alternatingSum(nums))


def case_two():
    nums=[100]
    print(Solution().alternatingSum(nums))


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
