def classify(number):
    # Write your code here
    divisor_of_number = []
    i = 1
    while i <= number//2:
        if number % i == 0:
            divisor_of_number.append(i)
        i += 1
    sums = sum(divisor_of_number)
    if sums == number:
        return "Perfect"
    elif sums > number:
        return "Abundant"
    else:
        return "Deficient"


print(classify(29))


from datetime import  date

date1 = date(2005, 1, 1)
date2 = date(2008, 1, 1)

date1_ord = date1.toordinal()
date2_ord = date2.toordinal()
cnt = 0

for d_ord in range(date1_ord, date2_ord):
    d = date.fromordinal(d_ord)
    if (d.weekday() == 6) and (d.day == 1):
        cnt = cnt + 1

print("Number of Sunday 1'st days is {}".format(cnt))
