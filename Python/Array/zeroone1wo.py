def sort(arr):
    # c0=c2=c1=0
    # for i in range(len(arr)):
    #     if arr[i] == 0:
    #         c0 += 1
    #     elif arr[i] == 1:
    #         c1 += 1
    #     else:
    #         c2 += 1  

    # for i in range(c0):
    #     arr[i] = 0
    # for i in range(c0, c0+c1):
    #     arr[i] = 1
    # for i in range(c0+c1, len(arr)):
    #     arr[i] = 2
    low = 0
    mid = 0
    temp = 0 
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            temp = arr[mid]
            arr[mid] = arr[low]
            arr[low] = temp
            low += 1
            mid +=1

        elif arr[mid] == 1:
            mid += 1
        else:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            #mid +=1
            high -= 1

    return arr
    
if __name__ == "__main__":
    arr = [1,1,2,2,1,0,1,0,2,1] 
    k = sort(arr)
    for i in range(len(arr)):
        print(arr[i],end = " ")
