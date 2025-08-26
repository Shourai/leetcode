class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) % 2 == 0:
            floor = len(nums1) // 2
            return (nums1[floor - 1] + nums1[floor]) / 2

        else:
            midpoint = len(nums1) // 2
            return float(nums1[midpoint])


def case_one():
    nums1 = [1, 3]
    nums2 = [2]
    Solution().findMedianSortedArrays(nums1, nums2)


def case_two():
    nums1 = [1, 2]
    nums2 = [3, 4]
    Solution().findMedianSortedArrays(nums1, nums2)


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
