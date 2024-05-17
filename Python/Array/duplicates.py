def removeDuplicates(arr):
    # st = set()
    # for i in range(len(arr)):
    #     st.add(arr[i])
    
    # k = len(st)
    # j=0

    # for x in st:
    #     arr[j] = x
    #     j +=1
    # return k
    i = 0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
        
    return i+1


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3,5,3,7,8,5,3,6,8,6,4,3,4,6,4,3,5,5,3,5,4,2,2,6,7,7,4,4,6,4,6,8,4,5,7,3,7,45]
    arr.sort()
    k = removeDuplicates(arr)
    for i in range(k):
        print(arr[i], end=" ")