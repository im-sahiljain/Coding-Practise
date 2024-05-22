def remDup(arr):
    num = set()
    for i in range(len(arr)):
        num.add(arr[i])
    j = 0
    for x in num:
        arr[j] = x 
        j += 1
    for k in range(j, len(arr)):
        arr[k] = 0
    return len(num), arr

if __name__ == "__main__":
    arr = [1,1,2,2,2,3,3]
    print(remDup(arr))