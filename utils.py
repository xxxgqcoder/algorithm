# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list_node(nums: list[int]) -> ListNode:
    """
    Make a list of node from nums. Return head of list node.
    """
    head = ListNode()
    thead = head
    for val in nums:
        node = ListNode(val, next=None)
        thead.next = node
        thead = thead.next

    return head.next


def list_node_val(head: ListNode) -> list[int]:
    """
    Get value of list node.
    """
    thead = head
    val = []
    while thead is not None:
        val.append(thead.val)
        thead = thead.next

    return val
