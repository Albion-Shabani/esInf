def sum_digits(num:int):
    sum = 0 
    while num:
        sum += num %10
        num = num//10
    return sum

def main():
    n = int(input("inserisci un numero: "))
    while n//10:
        n = sum_digits(n)
        print(n)
        
main()         
