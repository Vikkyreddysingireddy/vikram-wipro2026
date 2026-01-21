data = [1, 2, 3]
it = iter(data)
print(next(it))
print(next(it))
print(next(it))
for x in [10, 20, 30]:
    print(x)


class count:
    def __init__(self, n):
        self.n=n
        self.now=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.now < self.n:
            self.now += 1
            return self.now
        else:
            raise StopIteration

class Count:
    def __init__(self, n):
        self.max = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

a = Count(10)

for num in a:
    print(num)
