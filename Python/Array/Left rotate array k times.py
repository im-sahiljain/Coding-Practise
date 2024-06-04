def rev(a,s,e):
    while s < e:
        temp = a[s]
        a[s] = a[e]
        a[e] = temp
        s += 1
        e -= 1  

def rot(a,k):
    n = len(a)
    k %= n
    rev(a,0, k - 1)
    rev(a,k, n-1)
    rev(a,0,n-1)

    return a

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 3
    print(rot(arr,k))