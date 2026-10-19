class Triangle:
    def __init__(self,lato1,lato2,lato3):
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3
    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3
    def area(self):
        return (self.lato1+self.lato2+self.lato3)/2
    

def main():
    lato1 = int(input("lato 1: "))
    lato2 = int(input("lato 2: "))
    lato3 = int(input("lato 3: "))
    
    t = Triangle(lato1,lato2,lato3)
    
    print(f"perimetro {t.perimetro()}")
    print(f"area {t.area()}")
if __name__ == "__main__":
    main()
