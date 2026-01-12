def is_perfect_number(num):
    divisor_sum = 0
    for i in range(1, num):
        if num%i == 0:
            divisor_sum += i
    
    return divisor_sum == num

print(is_perfect_number(28))
print(is_perfect_number(29))