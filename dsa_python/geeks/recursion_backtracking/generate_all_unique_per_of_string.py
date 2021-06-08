def shouldSwap(string, start, curr):
    for i in range(start, curr):
        if string[i] == string[curr]:
            return 0
    return 1


def solution(string, index, n):

    if len(string) == 0:
        return
    if index >= n:
        print("".join(string))
        return

    for i in range(index, n):
        check = shouldSwap(string, index, i)
        if check:
            string[index], string[i] = string[i], string[index]
            solution(string, index + 1, n)
            string[index], string[i] = string[i], string[index]


string = list("AB")
solution(string, 0, len(string))
