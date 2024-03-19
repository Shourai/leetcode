# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next



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
