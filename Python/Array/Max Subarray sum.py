def sum(a):
    maxsum = a[0]
    cursum = a[0]

    for i in range(len(a)):
        cursum = max(a[i],cursum + a[i])
        maxsum = max(maxsum,cursum)
    return maxsum

if __name__ == "__main__":
    arr= [-2,1,3,4]
    print(sum(arr))