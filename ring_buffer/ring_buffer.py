class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []
        self.oldest = 0 # references storage list, to make sure we have the oldest item

    def append(self, item):
        # first we need to make sure that there is capacity left
        if len(self.store) < self.capacity:
            #then we can append it to the ring Buffer
            self.store.append(item)

        #if we don't have room, we need to make room
        else:
            self.store.insert(self.oldest, item) # inserting item after the oldest item
            self.store.pop(self.oldest + 1) #remove the previous oldest item

            # then we need to update the oldest (if we can)
            if self.oldest + 1 < self.capacity:
                self.oldest += 1

            else: #and if we can't, we just reset it to the first item in the list
                self.oldest = 0

    def get(self):
        # we can just return the storage list here
        return self.store