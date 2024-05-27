class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

def reverse(head):
    cur = head
    prev = None
    
    while cur is not None:
        nex = cur.next
        cur.next = prev
        prev = cur
        cur = nex

    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = reverse(head)
printLL(head)

        