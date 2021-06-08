t_cases = int(input())

for t in range(0, t_cases):
    size_of_list = int(input())
    a_list = input().split()
    dicto = {}
    for i in a_list:
        if i in dicto.keys():
            dicto[i] += 1
        else:
            dicto[i] = 1

    values = sorted(list(dicto.values()))
    last = values[-1:]
