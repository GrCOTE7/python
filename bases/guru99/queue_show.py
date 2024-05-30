import queue

def reverse_queue(q):
    return list(q.queue)[::-1]

def show():
    q1 = queue.Queue()  # FIFO
    # q1 = queue.LifoQueue() # LILO
    # Addingitems to the queue
    q1.put(11)
    q1.put(5)
    q1.put(4)
    q1.put(21)
    q1.put(3)
    q1.put(10)

    l = q1.queue
    print(l)
    ll = list(l)
    ll.sort()
    print("Queue triée:", *ll)
    print("Queue inversée:", reverse_queue(q1))

if __name__=='__main__':
    show()
