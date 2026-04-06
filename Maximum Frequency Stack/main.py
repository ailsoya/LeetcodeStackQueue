from collections import defaultdict, deque

class FreqStack:
    def __init__(self):
        self.freqs = defaultdict(int)
        self.freqs_dict = defaultdict(deque)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        curr_freq = self.freqs[val]
        self.max_freq = max(self.max_freq, curr_freq)
        self.freqs_dict[curr_freq].append(val)

    def pop(self) -> int:
        result_value = self.freqs_dict[self.max_freq].pop()
        self.freqs[result_value] -= 1

        if not self.freqs_dict[self.max_freq]:
            self.max_freq -= 1

        return result_value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
