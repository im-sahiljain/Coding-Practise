def maxlength(str):
    dic = {}
    l = 0
    length = 0
    for r in range(len(str)):
        char = str[r]
        if char in dic and dic[char] >= l:
            l = dic[char] + 1
        else:
            length = max(length, r - l +1)
        dic[char] = r

    return length

if __name__ == "__main__":
    str = "abcacbdef"
    print(maxlength(str))