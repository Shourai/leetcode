class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        T = target
        n = len(matrix)
        L = 0
        R = n - 1

        while L <= R:
            m = (L + R) // 2
            if T < matrix[m][0]:
                R = m - 1
            elif T > matrix[m][-1]:
                L = m + 1
            else:
                return self.search(matrix[m], target)
        return False

    def search(self, nums: list[int], target: int) -> bool:
        output = False
        n = len(nums)
        L = 0
        R = n - 1

        while L <= R:
            m = (L + R) // 2
            if nums[m] < target:
                L = m + 1
            elif nums[m] > target:
                R = m - 1
            elif nums[m] == target:
                return True
        return output


def case_one():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert Solution().searchMatrix(matrix, target) is True


def case_two():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert Solution().searchMatrix(matrix, target) is False


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
