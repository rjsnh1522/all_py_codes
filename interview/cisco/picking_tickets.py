def maxTickets(tickets):
    tickets.sort()
    nested_arr = []
    cont = 0
    for i in range(len(tickets)-1):
        if abs(tickets[i+1] - tickets[i]) > 1:
            nested_arr.append(tickets[cont:i+1])
            cont = i + 1
    print(nested_arr)
    max_sum = 0
    for i in nested_arr:
        if len(i) > max_sum:
            max_sum = len(i)
    return max_sum

# tickets = [8, 5, 4, 4, 8, 8, 8, 8]
tickets = [4, 13, 2, 3]
# tickets = [5, 10, 12, 1, 10]
print(maxTickets(tickets))
