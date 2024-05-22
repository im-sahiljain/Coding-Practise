def remDup(arr):
    i = 0 
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i+1, arr

if __name__ == "__main__":
    arr = [1,1,2,2,2,3,3]
    unique, array = remDup(arr)
    print("Unique element : ", unique ," Array : ", array)