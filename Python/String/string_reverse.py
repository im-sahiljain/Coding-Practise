s = "Sahil"
l=0
r= len(s) -1
sl = list(s)
while l<r:
    temp = sl[l]
    sl[l] = sl[r]
    sl[r] = temp
    l += 1
    r -= 1

sr =''.join(sl)

print(sr)