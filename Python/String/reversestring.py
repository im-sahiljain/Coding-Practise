def reverse(s):
    n = len(s)
    l = 0
    r = n- 1
    while l < r:
        temp = s[l]
        s[l] = s[r]
        s[r]=temp
        l += 1
        r -= 1
    return string

if __name__ == "__main__":
    string = list("sahil")
    print("".join(reverse(string)))