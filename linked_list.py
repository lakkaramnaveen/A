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

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index<0 or index >= self.get_length():
            raise Exception("Not a valid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index >= self.get_length():
            raise Exception("Not a valid index")
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                temp = itr.next
                itr.next = Node(data, temp)
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(23)
    ll.insert_at_end(21)

    ll.print()

    ll.insert_values([1,454,799])
    ll.print()

    ll.remove_at(1)
    ll.print()
    print(ll.get_length())

    ll.insert_at(1, 121)
    ll.insert_at(2, 233)
    ll.print()
    print(ll.get_length())
