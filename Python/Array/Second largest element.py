def largest(a):
    fm = a[1]
    sm = a[0]
    if a[0] > a[1]:
        fm = a[0]
        sm = a[1]

    for i in range(2,len(arr)):
        if a[i] > fm:
            sm = fm
            fm = a[i]
    return fm,sm

if __name__ == "__main__":
    arr= [3,6,45,2,8,5,76]
    print(largest(arr))