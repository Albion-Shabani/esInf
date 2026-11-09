import math
import lib.g2d as g2d
import car

MAP_W, MAP_H = 512, 480
BAR = 64
VIEW_H = MAP_H - BAR
SCALE = 2

BG = g2d.load_image("super-sprint-bg.png")

# Waypoint della prima mappa, in coordinate del canvas (stimati dall'immagine!)
WAYPOINTS = [
    (250, 64), (380, 64), (432, 100), (440, 160), (440, 270),
    (410, 320), (350, 335), (250, 335), (150, 335), (90, 320),
    (70, 270), (70, 160), (85, 100), (130, 64),
]

class Opponent:
    def __init__(self, waypoints, speed=2.0, size=14):
        self._wps = waypoints
        self._i = 1                       # prossimo waypoint da raggiungere
        self._x, self._y = waypoints[0]   # parte dal primo punto (centro)
        self._speed = speed
        self._size = size
        self._angle = 0.0

    def pos(self):
        """Angolo in alto a sinistra, come Car.pos()."""
        return (self._x - self._size / 2, self._y - self._size / 2)

    def center(self):
        return (self._x, self._y)

    def move(self):
        tx, ty = self._wps[self._i]
        dx, dy = tx - self._x, ty - self._y
        dist = math.hypot(dx, dy)
        if dist < self._speed + 4:            # waypoint raggiunto
            self._i = (self._i + 1) % len(self._wps)
            return
        self._angle = math.atan2(dy, dx)
        self._x += self._speed * dx / dist
        self._y += self._speed * dy / dist

    def draw(self):
        g2d.set_color((220, 30, 30))
        x, y = self.pos()
        g2d.draw_rect((x, y), (self._size, self._size))

car1 = car.Car((100, 36))
opp = Opponent(WAYPOINTS)

DEBUG = True

def tick():
    g2d.clear_canvas()
    g2d.draw_image(BG, (0, 0), (0, BAR), (MAP_W, VIEW_H))

    if DEBUG:
        g2d.set_color((0, 0, 255))
        for p in WAYPOINTS:
            g2d.draw_circle(p, 3)
        if g2d.mouse_clicked():
            print(g2d.mouse_pos(), ",")     # copia le coordinate dei click

    car1.move(g2d.current_keys())
    opp.move()

    sx, sy, sw, sh = car1.sprite()
    g2d.draw_image("super-sprint.png", car1.pos(), (sx, sy), (sw, sh))
    opp.draw()

g2d.init_canvas((MAP_W, VIEW_H), SCALE)
g2d.main_loop(tick)