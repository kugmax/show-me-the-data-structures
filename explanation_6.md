## Union and Intersection of Two Linked Lists

- n - number of element in list_1
- m - number of element in list_2

Implementations have two assumption: 
- no duplication values
- original lists can't be changed

### Union

#### Data structure

To satisfy this assumption needs to traverse all elements in two lists and copy it's values. Also `set` `added_values`
is using to remove duplications.

#### Time complexity
`O(n + m)` needs to traverse two lists. Operations with `added_values` happens for `O(1)`

#### Space complexity
`Node` object has 2 references, `LinkedList` has 3 references.
The result list has `O( 2 * (n_unique + m_unique) + 3)` space.

### Intersection

#### Data structure
Three helper `set` objects are using: 
- `added_values` store final all intersection unique elements
- `values_1` store unique elements from list_1
- `values_2` store unique elements from list_2

#### Time complexity
`O(max(n, m))` complexity to traverse all lists (which could have different length)

#### Space complexity
`O( 4(n_unique + m_unique) + 5)` is the space complexity

- `Node` object has 2 references, 
- `LinkedList` has 3 references.
- `values_1` has `O(n_unique)` elements
- `values_2` has `O(m_unique)` elements
- `added_values` has `O(n_unique + m_unique)` elements
- two helper references to traverse lists