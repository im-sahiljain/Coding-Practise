def in_fibo(num):
    if num == 0 or num == 1:
        return True
    a,b, = 0,1
    while b <= num:
        if b == num:
            return True
        c = a + b
        a = b
        b = c
    return False

if __name__ == "__main__":
    num = int(input("Enter number to find  "))
    if in_fibo(num):
        print(num , "is present in the Fibonacci sequence.")
    else:
        print(num, "is not present in the Fibonacci sequence.")