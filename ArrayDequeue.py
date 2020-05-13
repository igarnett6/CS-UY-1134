class ArrayDequeue:
    #a
    def __init__(self):
        self.data = []*10
        self.num_elems = 0
        self.front_ind = None
        self.back_ind = None
    #b
    def __len__(self):
        return self.num_elems

    #also b...
    def first(self):
        return self.data[front_ind]

    #c
    def is_empty(self):
        return (self.num_elems==0)

    #d
    def last(self):
        self.back_ind = (self.front_ind+self.num_elems)%(len(self.data))
        return self.data[self.back_ind]

    #e
    def enqueue_first(self, elem):
        if(self.num_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if(self.is_empty()):
            self.data.append(elem)
            self.front_ind = 0
            self.back_ind = 0
            self.num_elems += 1
        else:
            self.front_ind = (self.front_ind-1)%self.num_elems
            self.data[front_ind] = elem
            num_elems+=1



    #f
    def enqueue_last(self, elem):
        if(self.num_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if(self.is_empty()):
            self.data.append(elem)
            self.front_ind = 0
            self.back_ind = 0
            self.num_elems += 1
        else:
            back_ind = (self.front_ind + self.num_elems) % len(self.data)
            self.data[back_ind] = elem
            self.back_ind+=1
            self.num_elems += 1

    #g
    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        val = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len((self.data))
        self.num_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
        elif(self.num_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    #h
    def dequeue_last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        val = self.data[self.back_ind]
        self.data[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % len((self.data))
        self.num_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        elif(self.num_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
