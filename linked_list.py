class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        ltstr = ''

        while itr:
            ltstr += str(itr.data) + '-->'
            itr = itr.next

        print(ltstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(23)
    ll.print()
