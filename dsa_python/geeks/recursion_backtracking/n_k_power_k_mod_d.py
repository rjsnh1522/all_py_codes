def find_mod(n, k, d):
    # safe condition
    if k < 0:
        return "Not gonna do it bro"
    if n == 0:
        return 0
    # base condition
    if k == 1:
        return (n * k) % d
    # recurrence condition
    if k % 2 == 0:
        v = (find_mod(n, k // 2, d) % d)
        return (v * v) % d
    else:
        x = (find_mod(n, 1, d) % d)
        v = (find_mod(n, (k - 1) // 2, d) % d)
        return (x * v * v) % d


# t = int(input())
#
# for i in range(t):
#     arr_el = list(map(int, input().strip().split()))
#     print(find_mod(arr_el[0], arr_el[1], arr_el[2]))


# na = 675356291270936062618792023759228973612931947845036106320615547656937452547443078688431492068926649504871727226106159490917711597767365639481293908850963856115984810304444763175962178574185975388318964333860488897764303092540594692247754812893680210511085064625862847240629908131103403919693380566400462675698728299602761321599149107587048042961042220552902838040919625449936050294351
# ka = 5
# da = 18

na = 71000
ka = 5355
da = 26
result = find_mod(na, ka, da)
print(result)
