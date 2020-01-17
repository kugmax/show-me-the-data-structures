## Least Recently Used Cache

## Data structure

Main storage for cache data is hash map (dict). It provided the ability for get/set operation for `O(1)` constant time.
Linked list is uses to store information about recently used elements. Each time as element has `use operation` this
element moved to head of linked list. Because `Node` has reference to `next` and `prev` elements no needs to traverse whole
linked list, all operation happens for `O(1)`.

### Time complexity

- __move_node_to_head__()
- __make_node_new_head__()
- __cut_tail__()

- get()
- set()


### Space complexity

`use operation`
`cache hit`
`cache miss`