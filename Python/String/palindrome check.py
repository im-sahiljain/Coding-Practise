def check(s):
    l = 0
    r = len(s) - 1
    while l<r:
        if s[l] != s[r]:
            return False
        l += 1
        r -=1
    return True

if __name__ == "__main__":
    s = "abcdcba"
    print(check(s))