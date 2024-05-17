def twosum(arr, target):
    n = len(arr)
    ans = [-1,-1]
    for i in range(0,n):
        for j in range(1,n):
            if arr[i] + arr[j] == target:
                ans[0] = i
                ans[1] = j
                return ans
    return ans    
    
if __name__ == "__main__":
    arr= [1,2,3,4,5]
    k = twosum(arr,11)
    print(k)
