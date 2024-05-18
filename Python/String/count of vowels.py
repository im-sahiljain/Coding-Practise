def vcount(str):
    mpp ={"a":0,"e":0,"i":0,"o":0,"u":0}
    for i in str.lower():
        if i in mpp:
            mpp[i] += 1
    return mpp, list(mpp.values())

if __name__=="__main__":
    str = "AEIOU"
    print(vcount(str))