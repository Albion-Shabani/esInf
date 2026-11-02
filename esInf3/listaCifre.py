def digits(n:int) -> list[int]:
    cifre = []
    while n:
        cifre.append(n%10)
        n = n//10

    return cifre

n = 1
while n:
    n = int(input("inserisci numero: "))
    print(digits(n))