class Node: 
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next
    
    def __str__(self):
        return str(self.cargo)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

str1 = str(node1) + '->' + str(node2) + '->' + str(node3)
print str1