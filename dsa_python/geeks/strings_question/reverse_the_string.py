class Solution:
    def solve(self, A):
        string = A
        string = list(map(str.strip, string.split(" ")))
        return " ".join(string[::-1])



string = "the sky is blue"
sol = Solution()
print(sol.solve(string))
