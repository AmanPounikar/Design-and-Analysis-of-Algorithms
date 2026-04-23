def lcs_with_table(X, Y):
    m = len(X)
    n = len(Y)

   
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print("DP Table:")
    print("   ", end="")
    for ch in Y:
        print(ch, end="  ")
    print()

    for i in range(m + 1):
        if i == 0:
            print(" ", end=" ")
        else:
            print(X[i - 1], end=" ")
        for j in range(n + 1):
            print(dp[i][j], end="  ")
        print()

    i, j = m, n
    lcs_str = ""

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str = X[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], lcs_str


X = "AGGTAB"
Y = "GXTXAYB"

length, sequence = lcs_with_table(X, Y)

print("\nLength of LCS:", length)
print("LCS:", sequence)