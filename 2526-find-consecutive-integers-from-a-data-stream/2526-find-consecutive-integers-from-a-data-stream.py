class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.d = deque()
        self.c = Counter()

    def consec(self, num: int) -> bool:
        self.d.append(num)
        if num == self.value:
            self.c[num] += 1
        while len(self.d) > self.k: 
            n = self.d.popleft()
            self.c[n] -= 1
            if self.c[n] == 0:
                del self.c[n]
                
        return self.c[self.value] == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)