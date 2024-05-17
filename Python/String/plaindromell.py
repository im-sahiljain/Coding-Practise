class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def is_palindrome(head):
    if not head or not head.next:
        return True

    # Find the middle of the linked list
    middle = find_middle(head)

    # Reverse the second half of the linked list
    second_half = reverse_linked_list(middle.next)

    # Compare the first half with the reversed second half
    current1, current2 = head, second_half
    while current1 and current2:
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next

    return True

# Example usage:
# Creating a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

# Checking if the linked list is a palindrome
print(is_palindrome(head))  # Output: True
