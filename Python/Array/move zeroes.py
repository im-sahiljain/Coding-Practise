def rem(a): 
    for i in range(len(a)):
        if a[i] == 0:
            j = i
            break
    
    for i in range(j+1,len(a)):
        if a[i] != 0:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            j += 1
    return a

if __name__ == "__main__":
    arr= [0,1,0,3,12]
    print(rem(arr))