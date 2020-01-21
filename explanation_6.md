## Union and Intersection of Two Linked Lists

n - number of element in list_1
m - number of element in list_2

### Union

#### Data structure
This method has two assumption: 
    - no duplication values
    - original lists can't be changed

To satisfy this assumption needs to traverse all elements in two lists and copy it's values. Also `set` `added_values`
is using to remove duplications.

#### Time complexity
`O(n + m)` needs to traverse two lists. Operations with `added_values` happens for `O(1)`

#### Space complexity
`Node` object has 2 references, `LinkedList` has 3 references.
The result list has `O( 2 * (n_unique + m_unique) + 3)` space.
