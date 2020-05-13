 class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

head1 = None
head1 = Node()
head1.data = 1
head1.next = Node()
head1.next.data = 2
head1.next.next = Node()
head1.next.next.data = 3

curr_node = head1
while(curr_node is not None):
    print(curr_node.data, end=' ')
    curr_node = curr_node.next
print()

new_node = Node()
new_node.data = 4
new_node.next = head1
head1 = new_node

def add_first(lnk_lst_head, val):
    new_node = Node()
    new_node.data = val
    new_node.next = lnk_lst_head
    return new_node

head1 = add_first(head1, 5)
head1 = add_first(head1, 6)

curr_node = head1
while(curr_node is not None):
    print(curr_node.data, end=' ')
    curr_node = curr_node.next

print()
