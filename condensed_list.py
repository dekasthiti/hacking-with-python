def condense_list(head):
    prev_node = head
    curr_node = head
    seen = set()
    while curr_node:

        if curr_node.data in seen:

            # skip the seen node. update prev node's next to curr node's next
            prev_node.next = curr_node.next
        else:
            seen.add(curr_node.data)

            # update prev node to curr node
            prev_node = curr_node

        curr_node = curr_node.next

    return prev_node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_node(self, node):
        self.next = node


if __name__ == '__main__':
    def create_list():
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(1)
        e = Node(2)

        a.add_node(b)
        b.add_node(c)
        c.add_node(d)
        d.add_node(e)
        return a

    head = create_list()
    condense_list(head)
    while head:
        print(head.data)
        head = head.next


