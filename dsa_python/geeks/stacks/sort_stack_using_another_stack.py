class Solution:
    def solve(self, A):
        stack = A
        sorter_stack = []

        while len(A) > 0:
            top_element = stack.pop(-1)
            print(top_element)
            if len(sorter_stack) == 0:
                sorter_stack.append(top_element)
            else:
                top_of_sorter_stack = sorter_stack.pop(-1)
                if top_element < top_of_sorter_stack:
                    sorter_stack.append(top_element)
                else:
                    sorter_stack.append(top_element)
                    stack.append(top_of_sorter_stack)
        return sorter_stack


A = [5, 4, 3, 2, 1]
sol = Solution()
print(sol.solve(A))
