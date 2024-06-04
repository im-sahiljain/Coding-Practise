def greedy(greed, size):
    r = 0
    l = 0
    greed.sort()
    size.sort()

    while l <= len(greed):
        if size[l] >= greed[r]:
            r += 1
        l += 1
    return r

if __name__ =="__main__":
    greed = [1,5,3,3,4]
    size = [4,2,1,2,1,3]
    print(greedy(greed,size))