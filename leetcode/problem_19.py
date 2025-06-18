import unittest
from typing import List, Optional

from utils import ListNode, make_list_node, list_node_val


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        thead = ListNode()
        thead.next = head

        head1 = thead
        # head 1: skip first n node
        while n >= 0 and head1 is not None:
            n -= 1
            head1 = head1.next

        # head 2
        head2 = thead
        while head1 is not None:
            head1 = head1.next
            head2 = head2.next

        skip = head2.next
        head2.next = skip.next
        skip.next = None

        return thead.next


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        vals = [1, 2, 3, 4, 5, 6]
        n = 2
        want_val = [1, 2, 3, 4, 6]

        head = make_list_node(vals)
        ret_head = solution.removeNthFromEnd(head, n)
        ret_val = list_node_val(ret_head)
        self.assertEqual(ret_val, want_val)

        # case 2
        vals = [1]
        n = 1
        want_val = []

        head = make_list_node(vals)
        ret_head = solution.removeNthFromEnd(head, n)
        ret_val = list_node_val(ret_head)
        self.assertEqual(ret_val, want_val)

        # case 3
        vals = [1, 2]
        n = 1
        want_val = [1]

        head = make_list_node(vals)
        ret_head = solution.removeNthFromEnd(head, n)
        ret_val = list_node_val(ret_head)
        self.assertEqual(ret_val, want_val)


if __name__ == '__main__':

    unittest.main()
