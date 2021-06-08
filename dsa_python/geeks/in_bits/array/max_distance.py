# class Solution:
#     def maximumGap(self, arr): 
#         maxDiff = 0
#         n = len(arr)
#         for i in range(0, n): 
#             j = n - 1
#             while(j > i): 
#                 if arr[j] >= arr[i] and maxDiff < (j - i): 
#                     maxDiff = j - i; 
#                 j -= 1
        
#         return maxDiff 
  


# driver code 
# arr = [ 100, 100, 100, 100, 100 ]
# n = len(arr) 
# maxDiff = Solution().maximumGap(arr) 
# print(maxDiff) 


class Solution:
    def max(self, a, b): 
        if(a > b): 
            return a 
        else: 
            return b 

    def min(self, a,b): 
        if(a < b): 
            return a 
        else: 
            return b 

    # For a given array arr[], 
    # returns the maximum j - i 
    # such that arr[j] > arr[i] 
    def maximumGap(self,arr): 
        maxDiff = 0
        n = len(arr)
        LMin = [0] * n 
        RMax = [0] * n 

        # Construct LMin[] such that 
        # LMin[i] stores the minimum 
        # value from (arr[0], arr[1], 
        # ... arr[i]) 
        LMin[0] = arr[0] 
        for i in range(1, n): 
            LMin[i] = min(arr[i], LMin[i - 1]) 

        # Construct RMax[] such that 
        # RMax[j] stores the maximum 
        # value from (arr[j], arr[j+1], 
        # ..arr[n-1]) 
        RMax[n - 1] = arr[n - 1] 
        for j in range(n - 2, -1, -1): 
            RMax[j] = max(arr[j], RMax[j + 1])

        # Traverse both arrays from left 
        # to right to find optimum j - i 
        # This process is similar to 
        # merge() of MergeSort 
        i, j = 0, 0
        maxDiff = 0
        while (j < n and i < n): 
            if (LMin[i] <= RMax[j]): 
                maxDiff = max(maxDiff, j - i) 
                j = j + 1
            else: 
                i = i+1

        return maxDiff 





arr = [ 100, 100, 100, 100, 100 ]
n = len(arr) 
maxDiff = Solution().maximumGap(arr) 
print (maxDiff) 

