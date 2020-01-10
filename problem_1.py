class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def is_in_head(self):
        return self.prev is None and self.next is not None

    def is_in_tail(self):
        return self.prev is not None and self.next is None

    def is_in_middle(self):
        return self.prev is not None and self.next is not None


class LruCache(object):
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity can't be less then 1")

        self.store = dict()
        self.priority_head = None
        self.priority_tail = None

        self.capacity = capacity
        self.num_elements = 0

    def get(self, key):
        if key not in self.store:
            return -1

        node = self.store[key]
        self.__move_node_to_head__(node)

        return node.value

    def set(self, key, value):
        if key in self.store:
            existed_node = self.store[key]
            existed_node.value = value

            self.__move_node_to_head__(existed_node)

        else:
            new_node = Node(value)
            self.store[key] = new_node
            self.num_elements += 1

            if self.priority_head is None:
                self.priority_head = new_node
                self.priority_tail = new_node
                return

            self.__make_node_new_head__(new_node)

            if self.num_elements > self.capacity:
                self.__cut_tail__()

    def __move_node_to_head__(self, node):

        if node.is_in_tail():
            self.priority_tail = self.priority_tail.prev  # previous now is oldest
            self.priority_tail.next = None
            if self.priority_tail.prev is None:  # if new tail was head, need to point to new head
                self.priority_tail.prev = node

            self.__make_node_new_head__(node)

        elif node.is_in_middle():
            # connect node.prev with node.next
            node.prev.next = node.next
            node.next.prev = node.prev

            self.__make_node_new_head__(node)

        #  if node is not in the tail and not in the middle then it already in the head, nothing to do

    def __make_node_new_head__(self, node):
        self.priority_head.prev = node
        node.next = self.priority_head
        self.priority_head = node
        self.priority_head.prev = None

    def __cut_tail__(self):
        del self.store[self.priority_tail.value]
        self.priority_tail = self.priority_tail.prev
        self.priority_tail.next = None


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


def assert_true(actual):
    assert_equals(True, actual)


def when_capacity_is_less_then_1_then_raise_exception():
    is_ok = False
    try:
        LruCache(0)
    except ValueError:
        is_ok = True
    assert_true(is_ok)

    is_ok = False
    try:
        LruCache(-1)
    except ValueError:
        is_ok = True
    assert_true(is_ok)


def when_cache_is_empty_then_nothing_to_get():
    cache = LruCache(1)
    assert_equals(-1, cache.get(1))
    assert_equals(-1, cache.get("f"))
    assert_equals(-1, cache.get(0))

    cache = LruCache(5)
    assert_equals(-1, cache.get(1))
    assert_equals(-1, cache.get("f"))
    assert_equals(-1, cache.get(0))


def when_cache_capacity_is_1():
    cache = LruCache(1)

    cache.set(1, 1)
    assert_equals(1, cache.get(1))

    cache.set(2, 2)
    assert_equals(-1, cache.get(1))
    assert_equals(2, cache.get(2))

    cache.set(3, 3)
    assert_equals(-1, cache.get(1))
    assert_equals(-1, cache.get(2))
    assert_equals(3, cache.get(3))


def when_cache_capacity_is_2():
    cache = LruCache(2)

    cache.set(1, 1)
    assert_equals(1, cache.get(1))

    cache.set(2, 2)
    assert_equals(1, cache.get(1))
    assert_equals(2, cache.get(2))

    cache.set(3, 3)
    assert_equals(-1, cache.get(1))
    assert_equals(2, cache.get(2))
    assert_equals(3, cache.get(3))


def when_cache_capacity_is_3():
    cache = LruCache(3)

    cache.set(1, 1)
    assert_equals(1, cache.get(1))

    cache.set(2, 2)
    assert_equals(1, cache.get(1))
    assert_equals(2, cache.get(2))

    cache.set(3, 3)
    assert_equals(1, cache.get(1))
    assert_equals(2, cache.get(2))
    assert_equals(3, cache.get(3))

    cache.set(4, 4)
    assert_equals(-1, cache.get(1))  # 1 is oldest
    assert_equals(2, cache.get(2))
    assert_equals(3, cache.get(3))
    assert_equals(4, cache.get(4))


def when_cache_capacity_is_4():
    cache = LruCache(4)

    cache.set(1, 1)
    assert_equals(1, cache.get(1))

    cache.set(2, 2)
    assert_equals(1, cache.get(1))
    assert_equals(2, cache.get(2))

    cache.set(3, 3)
    assert_equals(1, cache.get(1))
    assert_equals(2, cache.get(2))
    assert_equals(3, cache.get(3))

    cache.set(4, 4)
    assert_equals(1, cache.get(1))
    assert_equals(2, cache.get(2))
    assert_equals(3, cache.get(3))
    assert_equals(4, cache.get(4))

    cache.set(5, 5)
    assert_equals(-1, cache.get(1))  # 1 is oldest
    assert_equals(2, cache.get(2))
    assert_equals(3, cache.get(3))
    assert_equals(4, cache.get(4))
    assert_equals(5, cache.get(5))


def when_value_was_updated():
    cache = LruCache(3)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)

    assert_equals(1, cache.get(1))
    assert_equals(2, cache.get(2))
    assert_equals(3, cache.get(3))

    cache.set(1, 'one')
    cache.set(2, 2)
    cache.set(3, "Udacity")

    assert_equals('one', cache.get(1))
    assert_equals(2, cache.get(2))
    assert_equals('Udacity', cache.get(3))


def set_operation_is_use_operation():
    cache = LruCache(3)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)

    cache.set(1, 1) # now 2 is oldest
    cache.set(4, 4)

    assert_equals(1, cache.get(1))
    assert_equals(-1, cache.get(2))
    assert_equals(3, cache.get(3))
    assert_equals(4, cache.get(4))


def get_operation_is_use_operation():
    cache = LruCache(3)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)

    cache.get(1) # now 2 is oldest
    cache.set(4, 4)

    assert_equals(1, cache.get(1))
    assert_equals(-1, cache.get(2))
    assert_equals(3, cache.get(3))
    assert_equals(4, cache.get(4))


def udacity_test():
    cache = LruCache(5)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)

    assert_equals(1, cache.get(1))
    assert_equals(2, cache.get(2))
    assert_equals(-1, cache.get(9))  # returns -1 because 9 is not present in the cache

    cache.set(5, 5)
    cache.set(6, 6)

    assert_equals(-1, cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


if __name__ == '__main__':
    when_capacity_is_less_then_1_then_raise_exception()
    when_cache_is_empty_then_nothing_to_get()

    when_cache_capacity_is_1()
    when_cache_capacity_is_2()
    when_cache_capacity_is_3()
    when_cache_capacity_is_4()

    when_value_was_updated()

    get_operation_is_use_operation()
    set_operation_is_use_operation()

    udacity_test()
