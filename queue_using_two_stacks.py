# MEDIUM


from collections import deque


class MyQueue(object):
    def __init__(self):
        self.dq = deque()

    def peek(self):
        return self.dq[0]

    def pop(self):
        return self.dq.popleft()

    def put(self, value):
        self.dq.append(value)


if __name__ == "__main__":
    my_q = MyQueue()
    my_q.put(42)
    print(my_q.dq)
    my_q.pop()
    print(my_q.dq)
    my_q.put(14)
    print(my_q.dq)
    print(my_q.peek())
    my_q.put(28)
    print(my_q.dq)
    print(my_q.peek())
    my_q.put(60)
    print(my_q.dq)
    my_q.put(78)
    print(my_q.dq)
    my_q.pop()
    print(my_q.dq)
    my_q.pop()
    print(my_q.dq)
