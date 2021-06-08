from collections import OrderedDict


class Solution:
    def solve(self, A):
        string = A
        hashed_entry = OrderedDict()
        queue = []
        b = ""
        for i in string:
            if i in hashed_entry:
                hashed_entry[i] += 1
                if len(queue) == 0:
                    b += i
                else:
                    if queue[0] == i:
                        queue.pop(0)
                        if len(queue) == 0:
                            b += "#"
                            continue
                    if len(queue) == 0:
                        b += i
                    else:
                        not_found = True
                        while not_found:
                            if len(queue) > 0:
                                ele = queue[0]
                                if hashed_entry[ele] > 1:
                                    queue.pop(0)
                                else:
                                    b += ele
                                    not_found = False
                            else:
                                b += "#"
                                not_found = False
            else:
                hashed_entry[i] = 1
                if len(queue) == 0:
                    b += i
                else:
                    b += queue[0]
                queue.append(i)
        return b


ss = "jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"
# jjjjjjjjjjjjjjjjjjjjjyyyyyyyyyyyyyyyyyyyyyyyyyyyqqqqq
# ss = "aabbcbbca"
# a#b#ccc##
ss = "xxikrwmjvsvckfrqxnibkcasompsuyuogauacjrr"
sol = Solution()
print(sol.solve(ss))
