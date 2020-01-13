import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        if data is None:
            raise ValueError("Data should be provided!")

        self.timestamp = timestamp
        self.data = data.encode('utf-8')
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        sha.update(data)
        return sha.hexdigest()

    def __repr__(self):
        return "timestamp: {0}, hash: {1} previous hash: {2}, data: {3}, ".format(self.timestamp, self.hash,
                                                                                  self.previous_hash, self.data)


class Blockchain():
    def __init__(self):
        self.last_block = Block(self.get_timestamp(), "Initial block", 0)
        self.storage = dict()
        self.storage[self.last_block.hash] = self.last_block

    def add_data(self, data):
        new_block = Block(self.get_timestamp(), data, self.last_block.hash)
        self.storage[new_block.hash] = new_block
        self.last_block = new_block

    def get_timestamp(self):
        return datetime.timestamp(datetime.utcnow())

    def print_chain(self):

        current_block = self.last_block
        while True:
            print(current_block)
            if current_block.previous_hash == 0:
                break

            current_block = self.storage[current_block.previous_hash]


if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.add_data("1 block")
    blockchain.add_data("2 block")
    blockchain.add_data("3 block")
    blockchain.add_data("4 block")
    blockchain.add_data("")

    blockchain.print_chain()

    is_ok = False
    try:
        blockchain.add_data(None)  # forbidden to use None as data
    except ValueError:
        is_ok = True

    assert is_ok


