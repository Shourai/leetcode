from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        d = ListNode()
        c = d
        while list1 and list2:
            if list1.val < list2.val:
                c.next = list1
                c = list1
                list1 = list1.next
            else:
                c.next = list2
                c = list2
                list2 = list2.next

        c.next = list1 if list1 else list2

        return d.next


def to_linked_list(iterable):
    head = None
    for val in reversed(iterable):
        head = ListNode(val, head)
    return head


def case_one():
    list1 = to_linked_list([1, 2, 4])
    list2 = to_linked_list([1, 3, 4])
    output = Solution().mergeTwoLists(list1, list2)

    while output:
        print(output.val)
        output = output.next


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
