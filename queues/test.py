from queues.Queue import Queue

queue = Queue()
print(queue.is_empty())
print('first in', 100)
print(queue.en_queue(100))
print(queue.en_queue(101))
print(queue.en_queue(103))
print(queue.items)
queue.de_queue()
print(queue.items)
