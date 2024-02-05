class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0

        for _ in range(len(height)):
            area = min(height[left_pointer], height[right_pointer]) * (
                right_pointer - left_pointer
            )
            if area > max_area:
                max_area = area
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            elif height[left_pointer] >= height[right_pointer]:
                right_pointer -= 1

        return max_area


def case_one():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert (Solution().maxArea(height)) == 49


def case_two():
    height = [1, 1]
    assert (Solution().maxArea(height)) == 1


def case_three():
    height = [1,3,2,5,25,24,5]
    assert (Solution().maxArea(height)) == 24


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
