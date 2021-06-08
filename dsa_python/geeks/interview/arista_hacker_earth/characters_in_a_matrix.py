def solution(matrix, k, n):
    strip_sum = [[None]*n for i in range(n)]
    for j in range(n):
        sum = 0
        for i in range(k):
            sum += matrix[i][j]
        strip_sum[0][j] = sum
    for i in range(1,n-k+1):
        sum += (matrix[i+k-1][j] - matrix[i-1][j])
        strip_sum[i][j] = sum

    print(strip_sum)
    # calculate sum of sub square using strip_sum

    for i in range(n-k +1):
        sum = 0
        for j in range(k):
            sum += 0 if strip_sum[i][j] is None else strip_sum[i][j]
        print(sum, end=" ")
        # calculate sum of remaining square
        # in current row by removing the leftmost
        # strip of previous sub-square and adding
        # a new strip
        for j in range(1, n-k+1):
            sum += (strip_sum[i][j+k-1] - strip_sum[i][j-1])
            print(sum, end=" ")



t = int(input())

for i in range(t):
    n_m_k = list(map(int, input().strip().split(" ")))
    n = n_m_k[0]
    m = n_m_k[1]
    k = n_m_k[2]
    matrix = [[0]*m]*n
    for row in range(n):
        string = input().strip()
        for col in range(m):
            matrix[row][col] = 1 if string[col] == '*' else 0
    solution(matrix, k, n)
