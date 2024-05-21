def climbStairs(n):
    if n == 0:
        return -1
    if n == 1:
        return 1
    ways = [0] * (n+1)
    ways[1] = 1
    ways[2] = 2
    for i in range(3,n+1):
        ways[i] = ways[i-1] + ways[i-2]

    return ways[n]

if __name__ == "__main__":
    n = int(input("enter Number of stairs : "))
    print(climbStairs(n))