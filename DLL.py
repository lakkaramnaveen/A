class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.prev = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        node.next = self.prev
        node.prev = None


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

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
                    return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        prev = None
        while itr:
            if itr.data == data:
                prev.next = itr.next
                return
            prev = itr
            itr = itr.next

    def print_forward(self):
        # This method prints list in forward direction. Use node.next

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.prev
        ltstr = ''

        while itr:
            ltstr += str(itr.data) + '-->'
            itr = itr.prev

        print(ltstr)

if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # r
