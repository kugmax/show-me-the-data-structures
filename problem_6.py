class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        new_node = Node(value)
        self.size += 1

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        self.tail.next = new_node
        self.tail = self.tail.next

    def size(self):
        return self.size

# TODO: need traverse to avoid modification of current lists
# TODO: need to remove duplication

# TODO: need to have in explanation example where allowed to modify current lists and duplication also allowed


def union(list_1, list_2):
    added_values = set()
    result = LinkedList()

    def loop(node):
        if node is None:
            return

        if node.value not in added_values:
            added_values.add(node.value)
            result.append(node.value)

        loop(node.next)

    loop(list_1.head)
    loop(list_2.head)

    return result


def intersection(list_1, list_2):
    added_values = set()
    may_be_added_values = set()

    result = LinkedList()

    current_node_1 = list_1.head
    current_node_2 = list_2.head

    # TODO: need to traverse all list to end to find values in both lists

    while True:
        pass

    return result


if __name__ == "__main__":
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
