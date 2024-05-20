def water(height):
    #brute
    # res = 0
    # for l in range(len(height)):
    #     for r in range(l+1, len(height)):
    #         area = (r-l) * min(height[l], height[r])
    #         res = max(res, area)
    # return res

    res = 0
    l = 0
    r = len(height) -1
    while l < r:
        area = (r-l) * min(height[l],height[r])
        res = max(area, res)

        if height[l] < height [r]:
            l += 1
        else:
            r -= 1
    return res


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    w = water(height)
    print(w)