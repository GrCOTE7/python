w = "spam"

# As a for with step -1
class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse(w)
for char in rev:
    print(char)

rev = Reverse(w)
print(list(iter(rev)))

def reverse_generator(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

res = reverse_generator(w)
for char in res:
    print(char)
res = reverse_generator(w)
print(list(res))
