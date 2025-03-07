class Queue:
    def __init__(self):
        self.items = [] # initializing an empty list to store queue elements

    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the item at the front of the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue") # exception if the queue is empty
        return self.items.pop(0) # remove and return the first item

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise"""
        return len(self.items) == 0

    def size(self):
        """Returns the number of items in queue"""
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()  # Create an instance of the queue

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("size of the queue is:", queue.size())  # Example: 3
    print("dequeue item:", queue.dequeue())  # Example: 10
    print("queue includes the following:", list(queue.items))  # Example: [20, 30]
    print("Is the queue empty?", queue.is_empty())  # Example: False