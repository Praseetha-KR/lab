# Circular Queue with Array
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = 0
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = tail
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)
