def largest(a):
    min = a[0]
    for i in range(1,len(a)):
        if a[i] < min:
            min = a[i]
    return min

if __name__ == "__main__":
    arr= [3,6,45,2,8,5,76]
    print(largest(arr))