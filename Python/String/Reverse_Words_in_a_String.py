def reverse(s):
    i=0
    n=len(s)
    result = ""

    while i<n:
        while i < n and s[i] == '_':
            i +=1
        if i >= n:
            break

        j = i +1

        while j<n and s[j] != '_':
            j+=1

        sub = s[i:j]

        if len(result) == 0:
            result = sub
        
        else:
            result = sub + "_" + result
            # result = result + "_" + sub

        i = j +1

    return result
    
if __name__ == "__main__":
    s = "_My_name__is_Sahil_Jain__"
    x = reverse(s)
    print(x)


