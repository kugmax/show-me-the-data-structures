import sys


class Node:
    def __init__(self, letters=None, weight=0):
        self.letters = letters
        self.weight = weight

        self.left = None
        self.right = None

    def set_children(self, node_1, node_2):
        self.letters = node_1.letters + node_2.letters
        self.weight = node_1.weight + node_2.weight

        if node_1.weight < node_2.weight:
            self.left = node_1
            self.right = node_2
        else:
            self.left = node_2
            self.right = node_1

    def is_leaf(self):
        return self.left is None and self.right is None

    def __repr__(self):
        return self.letters + "(" + str(self.weight) + ")"


def calculate_frequently(data):
    frequent_chars = dict()
    for ch in data:
        if ch not in frequent_chars:
            frequent_chars[ch] = 1
        else:
            frequent_chars[ch] += 1
    return frequent_chars


def sort(frequent_chars):
    return [Node(k, v) for k, v in sorted(frequent_chars.items(), key=lambda item: item[1])]


def get_next_smallest_leaf(leaf_nodes, roots_nodes):
    if len(roots_nodes) > 0:
        if len(leaf_nodes) == 0 or (leaf_nodes[0].weight > roots_nodes[0].weight):
            return roots_nodes.pop(0)
        else:
            return leaf_nodes.pop(0)
    else:
        return leaf_nodes.pop(0)


def build_tree(leaf_nodes):
    if len(leaf_nodes) == 1:
        return leaf_nodes[0]

    roots_nodes = list()

    root = None

    while True:
        if len(leaf_nodes) + len(roots_nodes) == 1:
            break

        leaf_1 = get_next_smallest_leaf(leaf_nodes, roots_nodes)
        leaf_2 = get_next_smallest_leaf(leaf_nodes, roots_nodes)

        root = Node()
        root.set_children(leaf_1, leaf_2)
        roots_nodes.append(root)

    return root


def build_codes(root):
    codes = dict()

    if root.is_leaf():
        codes[root.letters] = "0"
        return codes

    def loop(root, accumulator):
        if root.is_leaf():
            codes[root.letters] = accumulator
            return

        if root.left is not None:
            loop(root.left, accumulator + "0")

        if root.right is not None:
            loop(root.right,  accumulator + "1")

    loop(root, "")
    return codes


def encode(data, codes):

    result = ""
    for ch in data:
        result += codes[ch]
    return result


def huffman_encoding(data):
    if data is None or len(data) == 0:
        return None, None

    frequent_chars = calculate_frequently(data)
    sorted_chars = sort(frequent_chars)

    tree = build_tree(sorted_chars)
    codes = build_codes(tree)

    encoded = encode(data, codes)

    return encoded, tree


def huffman_decoding(data, tree):
    if data is None or len(data) == 0 or tree is None:
        return None, None

    if tree.is_leaf():
        return tree.letters

    decoded = ""

    current = tree
    for code in data:
        current = current.left if code == "0" else current.right

        if current.is_leaf():
            decoded += current.letters
            current = tree

    return decoded


def encode_and_decode(data):
    print("The size of the data is: {}".format(sys.getsizeof(data)))
    print("The content of the data is: {}".format(data))

    encoded_data, tree = huffman_encoding(data)

    if encoded_data is None:
        return

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    encode_and_decode("The bird is the word")
    encode_and_decode("")
    encode_and_decode("A")
    encode_and_decode("BA")
    encode_and_decode("The bird is the word The bird is the word The bird is the word The bird is the word "
                      "The bird is the word The bird is the word The bird is the word The bird is the word")

