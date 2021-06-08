
def print_binary(d):
    queue = [1]
    print(0)
    i = 0
    while len(queue) > 0:
        ele = queue.pop(0)
        if len(str(ele)) > d:
            break
        print(ele)
        for k in [0, 1]:
            num = f"{ele}{k}"
            queue.append(int(num))

        i += 1

print_binary(3)
