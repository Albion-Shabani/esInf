
import g2d

g2d.init_canvas((500, 500))

n = int(input("Inserisci il numero dei cerchi: "))

r = 225 / n
raggio = r
diametro = 2 * raggio

for i in range(n):
    x = 25 + raggio + i * diametro

    blu = 50 + i * (200 - 50) / (n - 1) if n > 1 else 50

    g2d.set_color((0, 0, int(blu)))
    g2d.draw_circle((x, 250), raggio)

g2d.main_loop()
