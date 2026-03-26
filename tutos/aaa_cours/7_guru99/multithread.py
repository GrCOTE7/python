import time
import _thread


def thread_test(name, wait):
    i = 1
    while i <= 3:
        time.sleep(wait * 3)
        print("Running %s (%s)\n" % (name, i))
        i = i + 1

    print("%s has finished execution" % name)


if __name__ == "__main__":

    _thread.start_new_thread(thread_test, ("First Thread", 1))
    _thread.start_new_thread(thread_test, ("Second Thread", 2))
    _thread.start_new_thread(thread_test, ("Third Thread", 3))
