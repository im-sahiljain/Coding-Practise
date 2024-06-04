def rot(a):
    temp = a[0]
    n = len(a)-1
    for i in range(1,len(a)):
        a[i-1] = a[i] 
    a[n] = temp
    return a

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(rot(arr))