def find(input_list):
    count = 0
    j = 0
    i = 0
    sublist = [0,0,7]    
    while i < len(input_list):
        if input_list[i] == sublist[j]:
            j += 1
            if j == 3:
                count += 1
                j = 0
        i += 1
    return count

if __name__ == "__main__":
    input_string = input("Enter elements separated by space : ")
    input_list = []
    for char in input_string.split():
        input_list.append(int(char))
    print(find(input_list))
