class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx = self.binary(x)
        yy = self.binary(y)
        l_xx = len(xx)
        l_yy = len(yy)
        xxx = xx.zfill(max(l_xx, l_yy))
        yyy = yy.zfill(max(l_xx, l_yy))

        distance = 0
        for i in range(len(xxx)):
            if xxx[i] != yyy[i]:
                distance += 1

        return xx, yy, distance

    def binary(self, n):
        return bin(n).replace("0b", "")



sol = Solution()
print(sol.hammingDistance(4, 2))
