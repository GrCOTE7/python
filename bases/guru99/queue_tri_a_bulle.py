import queue

q1 = queue.Queue()  # FIFO
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
print(*ll)


def reverse_queue(q):
    return list(q.queue)[::-1]


# using bubble sort on the queue
n = q1.qsize()
print(n)
for i in range(n):
    x = q1.get()  # the 'first' element is removed
    for j in range(n - 1):

        y = q1.get()  # the 'second' element is removed
        if x > y:
            q1.put(y)  # the smaller one is put at the start of the queue
        else:
            q1.put(x)  # the smaller one is put at the start of the queue
            x = y  # the greater one is replaced with x and compared again with nextelement
        q2=reverse_queue(q1).copy()
        print(q2)
    q1.put(x)

while q1.empty() == False:
    print(q1.queue[0], end=" ")
    q1.get()
