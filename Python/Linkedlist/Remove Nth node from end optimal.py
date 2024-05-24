class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

def DeleteNthNodefromEnd(head, N):
    fastp = head
    slowp = head

    for i in range(N):
        fastp = fastp.next
    
    while fastp.next is not None:
        fastp = fastp.next
        slowp = slowp.next

    delnode = slowp.next
    slowp.next = slowp.next.next
    delnode = None
    return head
    

arr = [1, 2, 3, 4, 5]
N = 3
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

head = DeleteNthNodefromEnd(head, N)
printLL(head)
    
