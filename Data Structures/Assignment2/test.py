from queue import PriorityQueue

queue = PriorityQueue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
print(queue.qsize())
queue.get()
print(queue.qsize())