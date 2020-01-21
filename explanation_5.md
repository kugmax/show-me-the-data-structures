## Blockchain

### Data structure
To store all blocks `dict` is using, where block's hash is the key and Block object is value. To connect each Block has
reference to previous Block.
Also Blockchain has additional reference to last Block in the chain.

### Time complexity
To add new  Block need's just create new Block object, put in in storage and update last reference. All this operations
happened for constant time `O(1)`

### Space complexity
Block object has 4 reference, and Blockchain has main storage plus one reference - `O(4n + 1)`
