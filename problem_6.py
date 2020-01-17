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

    values_1 = set()
    values_2 = set()

    result = LinkedList()

    current_1 = list_1.head
    current_2 = list_2.head

    while current_1 is not None or current_2 is not None:

        if current_1 is not None:
            if current_1.value in values_2 and current_1.value not in added_values:
                added_values.add(current_1.value)
                result.append(current_1.value)

            values_1.add(current_1.value)
            current_1 = current_1.next

        if current_2 is not None:
            if current_2.value in values_1 and current_2.value not in added_values:
                added_values.add(current_2.value)
                result.append(current_2.value)

            values_2.add(current_2.value)
            current_2 = current_2.next

    return result


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


def assert_equals_linked_list(expected, head):
    actual_list = list()
    while head is not None:
        actual_list.append(head.value)
        head = head.next

    assert_equals(expected, actual_list)


def assert_union(expected, list_1, list_2):
    actual = union(to_linked_list(list_1), to_linked_list(list_2))

    assert_equals_linked_list(expected, actual.head)


def assert_intersection(expected, list_1, list_2):
    actual = intersection(to_linked_list(list_1), to_linked_list(list_2))

    assert_equals_linked_list(expected, actual.head)


def to_linked_list(list):
    result = LinkedList()

    for i in list:
        result.append(i)

    return result


if __name__ == "__main__":
    assert_union([], [], [])
    assert_union([1], [1], [])
    assert_union([1], [], [1])
    assert_union([1], [1], [1])
    assert_union([1, 2], [1, 2], [2, 1])
    assert_union([3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11],
                 [3, 2, 4, 35, 6, 65, 6, 4, 3, 21],
                 [6, 32, 4, 9, 6, 1, 11, 21, 1])

    assert_intersection([], [], [])
    assert_intersection([], [1], [])
    assert_intersection([], [], [1])
    assert_intersection([1], [1], [1])
    assert_intersection([2, 1], [1, 2], [2, 1])
    assert_intersection([4, 6, 21],
                        [3, 2, 4, 35, 6, 65, 6, 4, 3, 21],
                        [6, 32, 4, 9, 6, 1, 11, 21, 1])
