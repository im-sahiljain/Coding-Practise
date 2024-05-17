def fibo(n,dp):
    if n<=1:
        return n

    if n in dp:
        return dp[n]
    
    dp[n] = fibo(n-1,dp) + fibo(n-2,dp)

    return dp[n]


def main():
    n = int(input("Enter the postion of fibo you want to find: "))
    dp = {}
    print("fibo no at post" , n , ":" , fibo(n,dp))

if __name__ == "__main__":
    main()