class Solution:
    def solve(self, A):
        string = A
        counter_dict = dict()
        found_or_not_dict = dict()
        stacker = []
        for i in string:
            if i in counter_dict:
                counter_dict[i] += 1
            else:
                counter_dict[i] = 1
                found_or_not_dict[i] = False

        for i in string:
            if len(stacker) == 0:
                stacker.append(i)
                counter_dict[i] -= 1
                found_or_not_dict[i] = True
            else:
                # now check if the string is already visited or not
                if not found_or_not_dict[i]:
                    stacker.append(i)
                    counter_dict[i] -= 1
                    found_or_not_dict[i] = True
                else:
                    counter_dict[i] -= 1
                    found_or_not_dict[i] = False
                    temp_stack = []
                    while len(stacker) > 0:
                        ele = stacker.pop(-1)
                        if ele != i:
                            temp_stack.append(ele)
                    while len(temp_stack) > 0:
                        t_ele = temp_stack.pop(-1)
                        stacker.append(t_ele)
                    stacker.append(i)
        return stacker

A = "cbacdcbc"
sol = Solution()
print(sol.solve(A))
