class RandomizedSet:

    def __init__(self):
        self.nums = []  # To store the elements
        self.index_map = {}  # To store the index of each element


    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        self.nums.append(val)
        self.index_map[val] = len(self.nums) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        index = self.index_map[val]
        last_num = self.nums[-1]
        self.nums[index] = last_num
        self.index_map[last_num] = index
        self.nums.pop()
        del self.index_map[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()