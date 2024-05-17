def reversefull(s):
    stack = []
    rev = " "

    for char in s:
        stack.append(char)
    while stack:
        c = stack.pop()
        rev = rev + c

    return rev


if __name__ == "__main__":
    s = "_My_name__is_Sahil_Jain__"
    x = reversefull(s)
    print(x)