import g2d

n = int(input("inserisci n: "))
r = 25

g2d.init_canvas((500,500))

for i in range(n+1):
    for j in range(i):
        g2d.draw_circle((r + j*r*2,i*r*2), r)
        

g2d.main_loop()