def digits(n):
    if n == 0:
        return []
    return [n % 10] +  digits(n // 10) 

print(digits(345))