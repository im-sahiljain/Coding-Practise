def miss(a):
    n = len(a)+1
    total_sum = (n * (n + 1)) // 2 
    asum = 0
    for i in range(len(a)):
        asum += a[i]
    
    return total_sum - asum

if __name__ == "__main__":
    arr = [4, 2, 1, 5]
    print(miss(arr))
