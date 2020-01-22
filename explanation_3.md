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
`sort()` python function is using to sort all unique characters. It's has `O(m log(m))` time complexity

#### Space complexity
`O(4m)` is space complexity because `Node` object has 4 reference per one element. 

### 3. Build Tree

#### Data structure
To build tree two queues are using `leaf_nodes` and `roots_nodes` (despite the fact that is's `list`, only operations
 `pop(0)` and `append` are using, which has `O(1)` time complexity). `roots_nodes` needed to store new created sub trees, 
 which always has more weight then in `leaf_nodes`. Thus we can find next smallest node without sort or traverse current 
 queues, just enough check heads of `leaf_nodes` and `roots_nodes` queues.
   
#### Time complexity
We have m elements which all must be traversed to build tree - `O(m)`. There is no any additional sorting or traversing,
just `pop(0)` and `append` operations, with has `O(1)` complexity.

#### Space complexity
The final tree has 2m-1 nodes where one node has 4 references so complexity is `O(4*(2m - 1))` per unique character.

### 4. Build codes

#### Data structure
`dic` is chosen to store binary representation for each unique character.

#### Time complexity
Needs to traverse all tree to calculate binary code - `O(m)`

#### Space complexity
Result codes store as pair in `dict` object - `O(2m)`

### 5. Encode

#### Data structure
Final encoded text stored in string object

#### Time complexity
`O(n)` because needs to traverse all character in sentence and get it binary code from `dict` for `O(1)`

### 6. Huffman decoding

#### Data structure
Final decoded text stored in string object

#### Time complexity
To find leaf in binary tree needs `O(log m)`, and it have to be done n times (for each character) - `O(n log m)`