class Solution:

    def binary_to_decimal(self, n):
        return int(n, 2)

    def grayCode(self, A):
        num_till_now = [0, 1]
        if A == 1:
            return num_till_now
        results = []
        for i in range(1, A):
            rev = num_till_now.copy()
            rev.reverse()
            num_till_now = num_till_now + rev
            lent = len(num_till_now)
            for j in range(len(num_till_now)):
                if j >= lent//2:
                    num_till_now[j] = "1" + str(num_till_now[j])
                else:
                    num_till_now[j] = "0" + str(num_till_now[j])

        for i in num_till_now:
            results.append(self.binary_to_decimal(i))
        return results


number = 16
s = Solution()
ss = s.grayCode(number)
print(ss)
