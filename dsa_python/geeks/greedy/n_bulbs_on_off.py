class Solution:
    def bulbs(self, A):
        count = 0
        for i in range(len(A)):
            if A[i] == 1 and count % 2 == 0:
                continue
            elif A[i] == 0 and count % 2 == 0:
                count += 1
            elif A[i] == 1 and count % 2 != 0:
                count += 1
            elif A[i] == 0 and count % 2 != 0:
                continue
        return count










b = [1]
s = Solution()
print(s.bulbs(b))
