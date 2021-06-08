

def solution(numb):
    ans = ''
    while numb > 0:
        if numb % 26 == 0:
            ans = 'Z'+ans
            numb = (numb//26) - 1
        else:
            ans = chr(64+(numb % 26)) + ans
            numb = numb // 26
    return ans




print(solution(133455))
print(solution(1335))
print(solution(133435))
