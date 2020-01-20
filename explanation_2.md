## Find all files beneath path with file name suffix.

## Data structure
`find_files` implemented used recursion `loop(path, accumulator)`, where `path` represent current directory and `accumulator` is
the `list` to store paths of found files. To traverse current directory uses `for` cycle. If in `for` cycle the directory has
been found then the new recursion step happens. 

### Time complexity
Because we have to traverse all directories and files the time complexity is `O(n)`.

### Space complexity
In the worst case all elements might have needed suffix, so space complexity is `O(n)`.