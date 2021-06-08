from heapq import heapify, heappop, heappush


class Solution:

    def solve(self, A, B):
        heapify(A)
        mini = heappop(A)
        while mini < 0:
            B -= 1
            mini = -1*mini
            heappush(A, mini)
            mini = heappop(A)
        if B > 0:
            if B % 2 == 0:
                heappush(A, mini)
            else:
                heappush(A, -1*mini)
        else:
            heappush(A, mini)
        return sum(A)


s = Solution()
A = [24, -68, -29, -9, 84]
B = 4

print(s.solve(A, B))
