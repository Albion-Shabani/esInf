import g2d

colori = []

with open("./colori.txt", "r") as file:
    for riga in file:
        valori = riga.strip().split(",")
        colori.append(tuple(map(int, valori)))

n = int(input("inserisci n: "))

g2d.init_canvas((400,400))

for i in range(n):
    raggio = 200 - (200/n)*i

    g2d.set_color(colori[i%len(colori)])
    g2d.draw_circle((200,200), raggio)

g2d.main_loop()