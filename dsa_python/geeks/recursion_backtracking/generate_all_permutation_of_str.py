def generate_permutation(string, start, end, results):
    # safe case
    if len(string) == 0:
        return
    if start == end - 1:
        if string not in results:
            results.append("".join(string))
    else:
        for current in range(start, end):
            string[start], string[current] = string[current], string[start]
            if "".join(string) not in results:
                generate_permutation(string, start + 1, end, results)
            string[start], string[current] = string[current], string[start]


t = int(input())
for i in range(t):
    st = str(input())
    end = len(st)
    results = list()
    result = generate_permutation(list(st), 0, end, results)
    results.sort()
    print(" ".join(results))
