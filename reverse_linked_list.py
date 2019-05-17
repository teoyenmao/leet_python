"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    curr_node = head
    next_node = None
    prev_node = None
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    head = prev_node  # point head right before curr_node (is None)
    return head



# 1 -> 2 -> 3 -> 4 -> N
# become
# 4 -> 3 -> 2 -> 1 -> N
