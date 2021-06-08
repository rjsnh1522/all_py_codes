def check_string_palindrome(string):
    # safe condition
    if string == "":
        return
    # base condition
    start = 0
    end = -1
    if len(string) == 1:
        return True
    if string[start] == string[end]:
        string = string[1:-1]
        check_string_palindrome(string)
        return True
        # else:
        #     return False
    else:
        return False


check_pali = "hrcucojwqunjbajhraornrsjwmbxacvtcnijljvchbyatpikyvskhvawrjggovlojquglfkcfxkgzughprh"
result = check_string_palindrome(check_pali)
print(result)

# t = int(input())
# for i in range(t):
#     n = int(input())
#     st = str(input())
#     if check_string_palindrome(st):
#         print("Yes")
#     else:
#         print("No")
