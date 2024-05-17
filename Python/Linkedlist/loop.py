class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def loop(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False





if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = None

    if loop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")