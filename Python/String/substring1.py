str = "Sahil"
n = len(str)
for len in range(1, n+1):
    for i in range(0,n-len+1):
        j = i + len - 1
        for k in range(i,j+1):
            print(str[k], end = " ")
        print()
    print()




