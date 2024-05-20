def fibo(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        result = fibo(n-1,memo) + fibo(n-2,memo)
        memo[n] = result
        return result

if __name__ == "__main__":
    n = int(input("Enter the number of vaules in fibonacci series: "))
    for i in range(0,n):
        print(fibo(i), end = ",")