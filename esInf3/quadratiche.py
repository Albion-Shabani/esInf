class Quadratica:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def predict(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c


def main():
    a = float(input("Inserisci a: "))
    b = float(input("Inserisci b: "))
    c = float(input("Inserisci c: "))

    q = Quadratica(a, b, c)

    while True:
        valore = input("Inserisci x (invio per terminare): ")

        if valore == "":
            break

        x = float(valore)
        print(q.predict(x))


main()