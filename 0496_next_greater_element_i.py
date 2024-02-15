class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums2) 
        result = [-1] * len(nums1)

        index_map = {}

        for idx, v in enumerate(nums1):
            index_map[v] = idx

        for i in range(n):
            if nums2[i] in nums1:
                for j in range(i + 1, n):
                    if nums2[j] > nums2[i]:
                        result[index_map[nums2[i]]] = nums2[j]
                        break

        return result

def case_one():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    output = [-1, 3, -1]
    assert (Solution().nextGreaterElement(nums1, nums2)) == output


def case_two():
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    output = [3, -1]
    assert (Solution().nextGreaterElement(nums1, nums2)) == output


def case_three():
    nums1 = [3,1,5,7,9,2,6]
    nums2 = [1,2,3,5,6,7,9,11]
    output = [5,2,6,9,11,3,7]
    assert (Solution().nextGreaterElement(nums1, nums2)) == output


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
