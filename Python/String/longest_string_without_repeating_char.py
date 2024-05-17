def sub(s):
    if(len(s) == 0 ):
        return 0
    l = 0
    maxlen = float("-inf")
    max_substring = ""
    sett = set()
    for r in range(len(s)):
        if s[r] in sett:
            while l < r and s[r] in sett:
                sett.remove(s[l])
                l += 1
        sett.add(s[r])
        substring_length = r-l+1
        # maxlen = max(maxlen, r-l+1)

        if substring_length > maxlen:
            maxlen = substring_length
            max_substring = s[l:r+1]

    return maxlen, max_substring 

if __name__ == "__main__":
    s = "abcaabcdba"
    q, long_substr = sub(s)
    print(q, long_substr)