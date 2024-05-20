def find(file_name, searh_string):
    line_no = 0
    try:
        with open(file_name,'r') as file:
            for line in file:
                line_no += 1
                if search_string in line:
                    return True, line, line_no
    except FileNotFoundError:
        print("File not found")
        return False


if __name__ == "__main__":
    file_name= "/home/sahil/Desktop/Code/Python/String/sample.txt"
    search_string = input("Enter search string : ")
    print(find(file_name,search_string))