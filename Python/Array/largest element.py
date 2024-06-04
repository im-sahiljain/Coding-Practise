def largest(a):
    max = a[0]
    for i in range(1,len(arr)):
        if a[i] > max:
            max = a[i]
    return max

if __name__ == "__main__":
    arr= [3,6,45,2,8,5,76]
    print(largest(arr))