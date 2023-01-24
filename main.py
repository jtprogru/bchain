# coding=utf-8
import datetime as date
import hashlib


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash.encode("utf-8")
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha3_512()

        sha.update(
            str(self.index).encode("utf-8")
            + str(self.timestamp).encode("utf-8")
            + str(self.data).encode("utf-8")
            + str(self.previous_hash).encode("utf-8")
        )

        return sha.hexdigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash

    return Block(this_index, this_timestamp, this_data, this_hash)


def main():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    num_of_blocks_to_add = 10

    for _ in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}".format(block_to_add.hash))


if __name__ == "__main__":
    main()
