class FiboGenerator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        a, b = 0, 1
        for _ in range(self.n):
            yield a
            a = b
            b = a + b

for num in FiboGenerator(10):
    print(num)
