from time import time


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    s = 0
    while low <= high:
        mid = (high + low) // 2
        s += 1
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return s

    return -1


def main():
    pass


if __name__ == "__main__":
    main()
