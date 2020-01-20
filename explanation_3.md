## Huffman Coding

### 1. Calculate frequently

#### Data structure
To store character frequently, hashmap (dict) is using. It's allow to have fast access to data.

#### Time complexity
`calculate_frequently` has O(n) time complexity because needs only once traverse all elements and `dict` has `O(1)` access
time complexity

#### Space complexity
If `n` is all amount of all characters in sentence to encode, `m` is amount of unique characters. `O(2m)` will be the 
space complexity because needs to store pairs per unique characters.

### 2. Sort

#### Data structure
The result of sort operation is `list` of `Node` objects in increasing order.  

#### Time complexity
`sort()` python function is using to sort all unique characters. It's has `O(log(m))` time complexity

#### Space complexity
`O(4m)` is space complexity because `Node` object has 4 reference per one element. 

### 3. Build Tree

#### Data structure
To build tree two queues are using `leaf_nodes` and `roots_nodes` (despite the fact that is's `list`, only operations
 `pop(0)` and `append` are using, which has `O(1)` time complexity). `roots_nodes` needed to store new created sub trees, 
 which always has more weight then in `leaf_nodes`. Thus we can find next smallest node without sort or traverse current 
 queues, just enough check heads of `leaf_nodes` and `roots_nodes` queues.
   
#### Time complexity


TODO: wrong:
We have m elements which all must be traversed to build tree - `O(m)`. Also, for each two existed or new built nodes, 
one more Node will be created and this new sub-nodes also must be traversed - `O(log(m))`. Final time complexity will be 
`O(m * log(m))`


#### Space complexity
