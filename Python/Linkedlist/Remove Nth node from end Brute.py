class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

def DeleteNthNodefromEnd(head, N):
    if head is None:
        return None
    cnt = 0
    temp = head

    while temp is not None:
        cnt += 1
        temp = temp.next

    if N == cnt:
        newhead = head.next
        head = newhead
        return head
    
    res = cnt - N
    temp = head

    while temp is not None:
        res -= 1
        if res == 0:
            break
        temp = temp.next

    delNode = temp.next
    temp.next = temp.next.next
    delNode = None
    return head

arr = [1, 2, 3, 4, 5]
N = 3
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

# Delete the Nth node from the end and print the modified linked list
head = DeleteNthNodefromEnd(head, N)
printLL(head)
    
