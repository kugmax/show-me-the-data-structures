## Return True if user is in the group, False otherwise.

### Data structure
To store groups and users `set` objects are using. It's provide fast access and remove duplications.

### Time complexity
n - is number of groups
m - is number of users

To find particular user needs to traverse all groups `O(n)` (in worst case) and check it's users for `O(1)`. 
`visited_groups` is `set`, so put/check operations also has `O(1)` time complexity.

### Space complexity
To avoid cycles we have to store all visited groups. In worst case it will be `O(3n)`, because each `Group` object 
has 3 references.