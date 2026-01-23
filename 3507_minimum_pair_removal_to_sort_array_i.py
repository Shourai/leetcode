class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        counter = 0
        while True:
            left_pointer = 0

            min_sum = 9999999999999
            min_sum_left_pointer = None
            len_nums = len(nums)
            decreasing = False

            while left_pointer < len_nums - 1:
                if nums[left_pointer] > nums[left_pointer + 1]:
                    decreasing = True

                current_sum = nums[left_pointer] + nums[left_pointer + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_sum_left_pointer = left_pointer
                left_pointer += 1

            if decreasing is True:
                counter += 1
                nums[min_sum_left_pointer] = min_sum
                del nums[min_sum_left_pointer + 1]
            else:
                break

        return counter


def case_one():
    pass


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
