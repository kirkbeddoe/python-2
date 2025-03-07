from collections import deque

class DequeQueue:

    def __init__(self):
        """Initialize an empty deque to store queue elements"""
        self.queue = deque() # creating a deque to store elements

    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        self.queue.append(item) # append to the end of queue

    def dequeue(self):
        """Removes and returns item to front of the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue") # raise error if queue is empty
        return self.queue.popleft() # remove from left (front of queue)

    def is_empty(self):
        """Returns True is queue is empty, false otherwise"""
        return len(self.queue) == 0 # check to see if deque is empty

    def size(self):
        """Returns the number of items in the queue"""
        return len(self.queue) # get the length of the deque

# creating a queue instance
queue = DequeQueue()

# check if the queue is empty
print("Is the queue empty?", queue.is_empty()) # true

# add elements to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# check the size of the queue
print("Queue size:", queue.size())  # 3

# remove elements from the queue
print("Dequeued:", queue.dequeue())  # 10
print("Dequeued:", queue.dequeue())  # 20

# check the size after dequeuing
print("Queue size after dequeuing:", queue.size())  # 1

# check if the queue is empty
print("Is the queue empty?", queue.is_empty())  # false

# dequeue the last element
print("Dequeued:", queue.dequeue())  # 30

# now the queue should be empty
print("Is the queue empty now?", queue.is_empty())  # true

# try to dequeue from an empty queue (this will raise an error)
try:
    queue.dequeue()
except IndexError as e:
    print("Error:", e)  # dequeue from an empty queue

