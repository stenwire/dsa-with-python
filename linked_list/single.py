class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # if the linked list is empty then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data: int, node: Node):
        new_node = Node(data)
        new_node.next = node
        self.head = new_node

    def insert(self, position, data, node: Node):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        index = position - 1
        while cur_node.next:
            count += 1
            temp, cur_node = cur_node, cur_node.next
            if count == index:
                temp.next = new_node
                new_node.next = cur_node

    def delete(self, position, data, node: Node):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        index = position - 1
        while cur_node.next:
            count += 1
            temp, cur_node = cur_node, cur_node.next
            if count == index:
                temp.next = cur_node.next

    def delete_head(self, node: Node):
        self.head = node.next

    def delete_tail(self, node: Node):
        cur_node = self.head
        while cur_node.next:
            temp, cur_node = cur_node, cur_node.next
        temp.next = None

    def is_palindrome(self, node: Node):
        cur_node = self.head
        arr = []
        while cur_node:
            arr.append(cur_node.data)
            cur_node = cur_node.next
        print(arr == arr[::-1])
        if (arr == arr[::-1]):
            return 1
        return 0

    def remove_duplicates(self, node: Node):
        cur_node = self.head
        mem = []
        while cur_node.next:
            temp = cur_node
            if cur_node.data not in mem:
                mem.append(cur_node.data)
                temp.next = cur_node.next
            temp, cur_node = cur_node, cur_node.next
        print(mem)

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


def main():
    sll = SingleLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.print_list()
    print("==== Prepend ====")
    sll.prepend(0, sll.head)
    sll.print_list()
    print("==== Insert ====")
    sll.insert(3, 7, sll.head)
    sll.print_list()
    print("==== Delete ====")
    sll.delete(3, 7, sll.head)
    sll.print_list()
    print("==== Delete head ====")
    sll.delete_head(sll.head)
    sll.print_list()
    print("==== Delete tail ====")
    sll.delete_tail(sll.head)
    sll.print_list()
    print("==== Is palindrome ====")
    sll_2 = SingleLinkedList()
    sll_2.append(1)
    sll_2.append(9)
    sll_2.append(1)
    sll_2.append(9)
    sll_2.append(1)
    sll_2.is_palindrome(sll_2.head)
    print("==== Remove duplicates ====")
    sll_2.remove_duplicates(sll_2.head)
    sll_2.print_list()



main()

# s = "stephen"
# print(s[3])