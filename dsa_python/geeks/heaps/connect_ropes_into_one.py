import heapq
from heapq import heapify, heappop


class Solution:

    def solve(self, A):
        heapify(A)
        sum = 0
        while len(A) >= 2:
            rope1 = heappop(A)
            rope2 = heappop(A)
            new_rope = rope1+rope2
            sum += (new_rope)
            heapq.heappush(A, new_rope)
        return sum


s = Solution()
A = [1, 2, 3, 4, 5]
print(s.solve(A))
