def water(a):
    l = 0
    r = len(a) -1
    res = 0
    ind = [0,0]
    while l < r:
        area = (r-l) * min(a[l],a[r])
        # res = max(area, res)
        # ind = [l,r]
        if area > res:
            res = area
            ind = [l, r]

        if a[l] < a[r]:
            l += 1
        else:
            r-=1

    val_l = a[ind[0]]
    val_r = a[ind[1]]
    return res,ind, val_l, val_r
    
if __name__ == "__main__":
    a = [1,8,6,2,5,4,8,3,7]
    v,i,l,r = water(a)
    print("Maximum area of water:", v)
    print("Indices of bars for maximum area:", i)
    print("Value at index l:", l)
    print("Value at index r:", r)