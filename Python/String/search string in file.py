def search_string_in_file(filename, search_string):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if search_string in line:
                    return True, line
        return False
    except FileNotFoundError:
        print("File not found")
        return False

if __name__ == "__main__":
    filename = "/home/sahil/Desktop/Code/Python/String/sample.txt"
    search_str = input("Enter string: ")
    print(search_string_in_file(filename, search_str))
