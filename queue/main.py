from queue import Queue

class myQueue:
    def __init__(self, mq=Queue()):
        self.mq = mq

    def add_element(self, data):
        queue = self.mq
        queue.put(data)

    def remove_element(self):
        queue = self.mq
        queue.get()

    def print_queue(self):
        qu = self.mq
        print(list(qu.queue))

def main():
    mq = myQueue()
    print("==== Add to queue ===")
    mq.add_element(1)
    mq.add_element(2)
    mq.add_element(3)
    mq.add_element(4)
    mq.add_element(5)
    mq.print_queue()
    print("==== Remove from queue ===")
    mq.remove_element()
    mq.remove_element()
    mq.print_queue()

main()