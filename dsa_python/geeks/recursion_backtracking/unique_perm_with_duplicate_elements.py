def shouldSwap(string, start, curr):
    for i in range(start, curr):
        if string[i] == string[curr]:
            return 0
    return 1

def make_permute(arr, prefix, result):
    unique = set(arr)
    if len(unique) == 1:
        result.append(prefix+arr)
        return
    if len(arr) == 0:
        result.append()
        return

    for i in range(len(arr)):
        prefix.append(arr[i])
        make_permute(arr[0:i] + arr[i+1:], prefix, result)
        prefix.pop()


arrs = [1, 1, 3]
results = list()

make_permute(arrs, [], results)
print(results)
