import random

def randchar(char1, char2):
    return chr(random.randint(ord(char1), ord(char2)))

rows = int(input("Inserisci la larghezza: "))
cols = int(input("Inserisci l'altezza: "))

data = [
    [randchar("a", "z") for i in range(rows)]
    for j in range(cols)
]
print(data)
for y in range(cols):
    for x in range(rows):
        end_ = "\n" if x == rows - 1 else "\t"
        print(data[y][x], end=end_)