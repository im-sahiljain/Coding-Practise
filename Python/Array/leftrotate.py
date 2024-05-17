def leftrotate(arr, r):
    n = len(arr)
    while r>0:
        temp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = temp
        r -= 1

    return arr

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    r = int(input("r : "))
    k = leftrotate(arr, r)
    for i in range (len(arr)):
        print(arr[i], end=" ")
