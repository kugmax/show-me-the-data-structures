## Least Recently Used Cache

## Data structure

Main storage for cache data is hash map (dict). It provides the ability for get/set operation for `O(1)` constant time.
Linked list is uses to store information about recently used elements. Each time, as element has `use operation`, this
element moved to head of linked list. Because `Node` has reference to `next` and `prev` elements no needs to traverse whole
linked list, all operation happens for `O(1)`.

### Time complexity

- __cut_tail__: O(7) => O(1)
- __make_node_new_head__: O(6) => O(1)
- __move_node_to_head__: O(9 + O(__make_node_new_head__)) => O(1)
- get: O(1)
    - for `cache miss`: O(1)
    - for `cache hit`: O(3 + O(__move_node_to_head__)) => O(1)
- set: O(1)
    - for `cache miss`: O(8 + O(__make_node_new_head__) + O(__cut_tail__)) => O(1)    
    - for `cache hit`: O(4 + O(__move_node_to_head__)) => O(1)

### Space complexity

 - Node object: O(3) => O(1)
 - LruCache object: O(4 + O(dict * n * O(Node)) ) => O(n)