'''
    A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest 
    elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) 
    data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

    A basic queue has the following operations:

    Enqueue: add a new element to the end of the queue.
    Dequeue: remove the element from the front of the queue and return it.
    In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

    1 x: Enqueue element  into the end of the queue.
    2: Dequeue the element at the front of the queue.
    3: Print the element at the front of the queue.
    Input Format

    The first line contains a single integer, , denoting the number of queries.
    Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. 
    All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, x, 
    denoting the value to be enqueued.

    It is guaranteed that a valid answer always exists for each query of type .
    Output Format

    For each query of type , print the value of the element at the front of the queue on a new line.

    Sample Input
        10
        1 42
        2
        1 14
        3
        1 28
        3
        1 60
        1 78
        2
        2
'''
class Queue:
        def __init__(self):
            self.in_stack = list()
            self.out_stack = list()

        def enqueue(self, data):
            self.in_stack.append(data)

        def dequeue(self):
            if not self.out_stack:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()

        def peek(self):
            if not self.out_stack:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
            return self.out_stack[-1]

def main():
    n = int(input())
    q1 = Queue()

    for i in range(n):
        query = [int(i) for i in input().split()]

        if query[0] == 1:
            q1.enqueue(query[1])
        if query[0] == 2:
            q1.dequeue()
        if query[0] == 3:
            print(q1.peek())

if __name__ == "__main__":
    main()