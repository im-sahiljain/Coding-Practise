import sys

def maxsub(arr):
    start, end = 0,0
    maxi = -sys.maxsize - 1
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum > maxi:
                maxi = sum
                start, end = i, j
    return maxi, arr[start:end+1]


if __name__ == "__main__":
    arr = [-2,-3,4,-1,-2,1,5,-3]
    res, list = maxsub(arr)
    print(res,list)