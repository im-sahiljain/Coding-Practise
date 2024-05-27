class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

def middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

mid_node = middle(head)
print(mid_node.data)
printLL(head)

        