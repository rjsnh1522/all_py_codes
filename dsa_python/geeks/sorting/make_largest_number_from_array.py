class Solution:
    # @param A : tuple of integers
    # @return a strings
    def large_number_maker(self, l_arr, r_arr):
        i = 0
        j = 0
        results = []
        while i < len(l_arr) and j < len(r_arr):
            if int(str(str(l_arr[i]) + str(r_arr[j]))) > int(str(str(r_arr[j]) + str(l_arr[i]))):
                results.append(l_arr[i])
                i += 1
            else:
                results.append(r_arr[j])
                j += 1

        if i < len(l_arr):
            results += l_arr[i:]
        elif j < len(r_arr):
            results += r_arr[j:]
        return results

    def largestNumber(self, A):
        arr = A
        ans = self.divider(arr)
        final = ''.join(map(str, ans)).lstrip('0')
        if final:
            return final
        else :
            return  '0'

    def divider(self, arr):
        if len(arr) == 1:
            return arr

        mid = len(arr) // 2
        l_arr = self.divider(arr[0:mid])
        r_arr = self.divider(arr[mid:])
        numb_now = self.large_number_maker(l_arr, r_arr)
        return numb_now




s = Solution()
arrs = [3, 30, 34, 5, 9]
print(s.largestNumber(arrs))
