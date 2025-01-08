class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.stream = []

    def next(self, val: int) -> float:
        self.stream.append(val)
        return sum(self.stream[(-1 * self.size):]) / min(len(self.stream), self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
