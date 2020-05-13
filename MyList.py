import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_capacity):
        new_data = make_array(new_capacity)
        for i in range(self.n):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __getitem__(self, ind):
        if not (0 <= ind <= (self.n - 1)):
            raise IndexError(str(ind) + " is out of range")
        return self.data[ind]

    def __setitem__(self, ind, value):
        if not (0 <= ind <= (self.n - 1)):
            raise IndexError(str(ind) + " is out of range")
        self.data[ind] = value

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def extend(self, other):
        for elem in other:
            self.append(elem)
