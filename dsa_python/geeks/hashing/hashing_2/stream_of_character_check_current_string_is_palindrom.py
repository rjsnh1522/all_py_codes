# class Solve:
#
#     def __init__(self):
#         self.string = ''
#
#     def solve(self, char):
#         pass
from collections import OrderedDict

st = ["shivesh", "bhavesh", "ramesh", "suresh", "dddddddddddd"]
dd = dict()
k = 9
for i,j in enumerate(st):
    dd[j] = k
    k-=1

for k,v in dd.items():
    print(k, v)

