def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    
    return num == sum(int(digit) ** num_digits for digit in num_str)

print(is_armstrong(153))
print(is_armstrong(414))