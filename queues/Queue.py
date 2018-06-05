# FIFO =  First in, first out
import pprint


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def en_queue(self, item):
        self.items.insert(0, item)

    def de_queue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def values(self):
        return self.items
