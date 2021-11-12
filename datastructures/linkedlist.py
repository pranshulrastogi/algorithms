class LinkedList:
    def __init__(self, node_values, from_other_list=False):
        """
        @params: node_values: list of values for nodes
        @returns: head of linked list of type SingleLinkedListNode
        """
        if from_other_list:
            assert not isinstance(node_values, list), "pass head node of the other list"
            self.head = node_values
        else:
            self.head = None
            for val in node_values:
                if self.head is None:
                    node = SingleLinkedListNode(val)
                    self.head = node
                else:
                    self.append(val)

    def append(self, node_value):
        p = self.head
        if p:
            while p.next:
                p = p.next
        node = SingleLinkedListNode(node_value)
        p.next = node

    def print(self):
        p = self.head
        while p.next:
            print(p.val, end="->")
            p = p.next
        if p:
            print(p.val)

    def tolist(self):
        """
        returns list representation of current linked list
        """
        p = self.head
        result = []
        while p:
            result.append(p.val)
            p = p.next
        return result


class SingleLinkedListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


if __name__ == "__main__":
    ll = LinkedList([1, 2, 3])
    ll.append(8)
    ll.print()
    print(ll.tolist())
