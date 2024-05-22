def anagram(s,p):
    if len(p ) > len(s): return []
    pCount, sCount = {}, {}

    for i in range(len(p)):
        if p[i] not in pCount:
            pCount[p[i]] = 1
        else:
            pCount[p[i]] += 1

        if s[i] not in sCount:
            sCount[s[i]] = 1
        else:
            sCount[s[i]] += 1

    if sCount == pCount:
        res = [0]
    else:
        res = []
        
    l=0
    for r in range(len(p),len(s)):
        if s[r] not in sCount:
            sCount[s[r]] = 1
        else:
            sCount[s[r]] += 1
        sCount[s[l]] -= 1
        if sCount[s[l]] == 0:
            sCount.pop(s[l])
        l += 1

        if sCount == pCount:
            res.append(l)
            

    return res

if __name__ == "__main__":
    s = "abcdecdbacb"
    p = "cab"
    print(anagram(s,p))