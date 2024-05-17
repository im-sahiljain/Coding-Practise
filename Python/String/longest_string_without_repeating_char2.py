def subString(s):
    if len(s) == 0:
        return 0
    
    l = 0
    length = float("-inf")
    sett = set()
    sstr = ''
    for r in range(len(s)):
        if s[r] in sett:
            while l < r and s[r] in sett:
                sett.remove(s[l])
                l += 1
        sett.add(s[r])
        
        length = max(length,r-l+1)

    return length

if __name__ == "__main__":
    s = "qwertyuiop"
    j = subString(s)
    print(j)