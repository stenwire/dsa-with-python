from collections import deque

class myStack:
    def __init__(self, ms=deque()):
        self.ms = ms

    def add_element(self, data):
        stack = self.ms
        stack.append(data)

    def remove_element(self):
        stack = self.ms
        stack.pop()

    def print_stack(self):
        stack = self.ms
        print(list(stack))

def main():
    ms = myStack()
    print("==== Add to stack ===")
    ms.add_element(1)
    ms.add_element(2)
    ms.add_element(3)
    ms.add_element(4)
    ms.add_element(5)
    ms.print_stack()
    print("==== Remove from stack ===")
    ms.remove_element()
    ms.remove_element()
    ms.print_stack()


main()