class Polinomio:
    def __init__(self, coefficienti: list[float]):
        self.coefficienti = coefficienti

    def predict(self, x: float) -> float:
        risultato = 0
        n = len(self.coefficienti) - 1

        for i in range(len(self.coefficienti)):
            risultato += self.coefficienti[i] * x**(n-i)

        return risultato


def main():
    coefficienti = []

    while True:
        valore = input("Inserisci coefficiente (invio per terminare): ")

        if valore == "":
            break

        coefficienti.append(float(valore))

    p = Polinomio(coefficienti)

    while True:
        valore = input("Inserisci x (invio per terminare): ")

        if valore == "":
            break

        x = float(valore)
        print(p.predict(x))


main()