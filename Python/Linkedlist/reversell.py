class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse(head):
    temp =head
    prev= None

    while temp is not None:
        front = temp.next
        temp.next = prev
        prev=temp
        temp =front

    return prev

def printl(head):
    temp = head
    while temp is not None:
        print(temp.data, end = " ")
        temp = temp.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    printl(head)

    head = reverse(head)
    printl(head)