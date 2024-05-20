def remove(file_name):
    seen_line = set()
    removed_line = []
    try:
        with open(file_name,'r') as file:
            for line in file:
                if line not in seen_line:
                    seen_line.add(line)
                if line in seen_line:
                    removed_line.append(line)
        
        with open(file_name,'w')as file:
            for line in seen_line:
                file.write(line)

    except FileNotFoundError:
        print("File not found")
        return False
    
    return removed_line, 

if __name__ == "__main__":
    file_name = "/home/sahil/Desktop/Code/Python/String/sample.log"
    left = remove(file_name)
    print(f"Duplicate lines removed. The file '{file_name}' has been updated.")
    print("Lines removed are : ", left) 



