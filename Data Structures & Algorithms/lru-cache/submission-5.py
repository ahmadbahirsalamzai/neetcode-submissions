class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # [[key,value]]
        self.capacity = capacity
    # time: O(1)
    def get(self, key: int) -> int:
        # if the key is already there move to the end
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    # time O(1)
    def put(self, key: int, value: int) -> None:
        # if the key is in the dict then update the value and move ot the end and return
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        
        # if cache is full then pop the first element and then add move the new key to the end
        if len(self.cache) == self.capacity:
            self.cache.pop(next(iter(self.cache)))

        self.cache[key] = value