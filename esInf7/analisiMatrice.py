data = [['b', 'e', 'g', 'g'], ['k', 'q', 't', 'z'], ['u', 'm', 'a', 'd'], ['i', 'o', 'f', 'p']]

with open("./matrix.csv", "w") as file:   
    for i in range(len(data)):
        for j in range(len(data[i])):
            end_ = "\n" if j == len(data[i]) - 1 else ","
            print(data[i][j], end=end_)
            file.write(str(data[i][j]+ end_))


char = input("inserisci un caratere da cercare: ")
while char:
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == char:
                bordo = "*" if i == 0 or j == 0 else ""
                print(f"caratere trovato in posizione {bordo} {i+1,j+1}")
    char = input("inserisci un caratere da cercare: ")