def armstrong(num):
    n = len(str(num))
    arm = 0
    x = num  
    while x > 0:
        digit = x % 10  
        arm += digit ** n
        x //= 10  # Remove last digit
    return arm == num

