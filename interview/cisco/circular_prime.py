
def rotation(N):
    return [N[i:] + N[:i] for i in range(len(N))]


def prime_numbers(n):
    prime = []
    start = 1
    end = n
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                prime.append(str(i))
    return prime


def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

def countCircularPrimes(number):
    prime_factors = prime_numbers(number)
    cir_cnt = 0
    for i in prime_factors:
        all_rotations = rotation(i)
        if len(all_rotations) == 1:
            cir_cnt += 1
        else:
            for j in range(1, len(all_rotations)):
                if isPrime(int(all_rotations[j])):
                    cir_cnt += 1
    return cir_cnt

print(countCircularPrimes(200))
