class Solution:
    def compareVersion(self, A, B):
        v1 = A.split('.')
        v2 = B.split('.')

        if len(v1) < len(v2):
            while len(v1) < len(v2):
                v1.append("0")
        elif len(v2) < len(v1):
            while len(v2) < len(v1):
                v2.append("0")
        v1_len = len(v1)
        v2_len = len(v2)
        for i in range(v1_len):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) == int(v2[i]):
                if i == (v1_len-1) and (i == v2_len-1):
                    return 0
                else:
                    continue
        return -1





v1 = "2.9.8"
v2 = "2.9.8"
sol = Solution()
print(sol.compareVersion(v1, v2))
