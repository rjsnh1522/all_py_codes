"""
Generators are a special kind of iterator that allow you to iterate over a sequence of values lazily.
Instead of generating all values at once (like a list), they yield one value at a time, pausing execution between each value.
"""

# function based generators

def count_to_n(n):
    count = 1
    while count <= n:
        yield count
        count += 1


def caller():
    for i in count_to_n(5):
        print(i)

# class based Generators
class CountUpTo:
    def __init__(self, start, n):
        self.n = n
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.n:
            current = self.count
            self.count +=1
            return current
        else:
            raise StopIteration


for number in CountUpTo(5, 12):
    print(number)



# Generators are special case iterator

if __name__ == "__main__":
    caller()




