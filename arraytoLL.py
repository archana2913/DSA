
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def print_first_element(self):
        if self.head:
            print("The first element is:", self.head.data)
        else:
            print("The linked list is empty.")
def array_to_linked_list(arr):
    linked_list = LinkedList()
    for item in arr:
        linked_list.append(item)
    return linked_list
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    linked_list = array_to_linked_list(arr)
    linked_list.print_first_element()