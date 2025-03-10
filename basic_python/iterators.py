"""
An iterator is any object that implements the iterator protocol:
__iter__: Returns the iterator object (usually self).
__next__: Returns the next value or raises StopIteration when done.
"""

"""
An iterator is an object that allows you to traverse (iterate over) a collection of elements, one at a time.
Iterators implement the iterator protocol, which consists of two methods:
"""

class CountUpTO:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            res = self.current
            self.current +=1
            return res
        else:
            raise StopIteration


if __name__ == "__main__":
    cut = CountUpTO(6)
    for n in cut:
        print(n)


