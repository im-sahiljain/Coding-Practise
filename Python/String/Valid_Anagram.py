def anagram(s,t):
    if len(s) != len(t):
        return False
    
    countS, countT = {},{} 

    for char in s:
        if char in countS:
            countS[char] += 1
        else:
            countS[char] = 1
    # print(countS)

    for char in t:
        if char in countT:
            countT[char] += 1
        else:
            countT[char] = 1
    # print(countT)
            
    return countT == countS


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    ress = anagram(s,t)
    print(ress)
