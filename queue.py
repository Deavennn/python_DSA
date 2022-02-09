class Queue:
    def __init__(self):
        self.queue = list()
    def add(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False
    def remove(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return "No item in queue"
    def size(self):
        return len(self.queue)
    def print(self):
        for i in self.queue:
            print(i)
queue = Queue()
for i in range(1,11):
    queue.add(i)
queue.print()
queue.remove()
queue.print()
