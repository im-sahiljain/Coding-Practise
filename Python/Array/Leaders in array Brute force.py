def leaders(a):
    res =[]
    for i in range(len(a)):
        is_leader = True
        for j in range(i+1,len(a)):
            if a[i] <= a[j]:
                is_leader = False
                break
        if is_leader:
            res.append(a[i])

    return res

def leaders2(a):
    res = []
    mpp = {}
    for i in range(len(a)):
        is_leader = True
        if a[i] not in mpp:
            mpp[a[i]] = i
        
    return res

if __name__=="__main__":
    a = [20, 17, 15, 19, 18, 16, 21, 14, 13, 12, 11, 25, 24, 55,23, 22, 10, 9,35, 8, 7, 6, 5, 4, 3, 2, 1]
    print(leaders2(a))