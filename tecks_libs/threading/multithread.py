import time
import threading


def thread_test(name, wait):
    i = 1
    while i <= 3:
        time.sleep(wait * 3)
        print("Running %s (%s)\n" % (name, i))
        i = i + 1

    print("%s has finished execution" % name)


if __name__ == "__main__":
    t1 = threading.Thread(target=thread_test, args=("First Thread", 1))
    t2 = threading.Thread(target=thread_test, args=("Second Thread", 2))
    t3 = threading.Thread(target=thread_test, args=("Third Thread", 3))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All threads have finished execution")
