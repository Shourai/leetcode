# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(iterable):
    head = None
    for val in reversed(iterable):
        head = ListNode(val, head)
    return head


def to_native_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next


h = to_linked_list([1, 2, 4])

print(h)
print(h.val)
c = h.next
print(c.val)
c = c.next
print(c.val)
c = c.next


def case_one():
    # Singly Linked List with insertion and print methods
    pass


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
