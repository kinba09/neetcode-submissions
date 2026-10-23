"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtonew = defaultdict(lambda: Node(0))
        oldtonew[None] = None

        curr = head
        while curr:
            oldtonew[curr].val = curr.val
            oldtonew[curr].next = oldtonew[curr.next]
            oldtonew[curr].random = oldtonew[curr.random]
            curr=curr.next
        return oldtonew[head]
        