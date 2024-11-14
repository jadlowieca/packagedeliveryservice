
class HashMap:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for i in range(capacity)]

    def insert(self, key, value):
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
    def lookup(self, key):
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return v

        return None

    def remove(self, key):
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def __getitem__(self, item):
        return self.lookup(item)


