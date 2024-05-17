def longestCommonPrefix(str) -> str:
    if len(str) == 0:
        return " " 
    
    base = str[0]
    for i in range(len(base)):
        for word in str[1:]:
            if i == len(word) or word[i] != base[i]:
                return base[0:i]       
    return base


if __name__ == "__main__":
    str = ["flower","flow","flight","flop"]
    r = longestCommonPrefix(str)
    print(r)