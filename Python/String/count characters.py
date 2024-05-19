def char_count(str):
    mpp = {}
    for i in str.lower():
        if i in mpp:
            mpp[i] += 1
        else:
            mpp[i] = 1
    return mpp

if __name__=="__main__":
    str = "Sahil"
    print(char_count(str))