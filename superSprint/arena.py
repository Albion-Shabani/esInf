import lib.g2d as g2d
import lib.polar as polar

CHECKPOINT = [
    (216.0, 64.0), (375.0, 65.0), (441.0, 160.0), (437.0, 266.0), 
    (412.0, 316.0), (341.0, 339.0), (260.0, 224.0), (170.0, 222.0),
      (149.0, 332.0), (85.0, 313.0), (73.0, 231.0), (66.0, 128.0), 
      (97.0, 66.0)
    ]

class Arena():
    def __init__(self):
        self.MAP_W, self.MAP_H = 512, 480
        self.BAR = 64                  # altezza della striscia nera in alto
        self.VIEW_H = self.MAP_H - self.BAR      # 416
        self.SCALE = 2.5
        self.BG = g2d.load_image("super-sprint-bg.png")
        self.bg_surf = g2d._loaded[self.BG]          # la Surface di pygame caricata da g2d
        self.checkPoint = CHECKPOINT
        self.i_checkPoint = 0
    def draw_map(self):
        g2d.draw_image("super-sprint-bg.png", (0, 0), (0, self.BAR), (self.MAP_W, self.VIEW_H))

    # funzione per le collizione 
    def is_road(self,x, y):
        """True se il pixel (x, y) del canvas è asfalto."""
        x, y = int(x), int(y)
        if not (0 <= x < self.MAP_W and 0 <= y < self.VIEW_H):
            return False
        r, g, b = self.bg_surf.get_at((x, y + self.BAR))[:3]   # + BAR: salto la striscia nera
        return r == g == b and 80 <= r <= 200  

    # funzione per vedere se le macchine hanno preso il checkpoint

    def draw_checkPoint(self): 
        g2d.set_color((255,0,0))
        g2d.draw_circle((self.checkPoint[self.i_checkPoint]), 10)
    
    def get_checkPoint(self):
        return self.checkPoint[(self.i_checkPoint - 1) % len(self.checkPoint)]

    def check_checkPoint(self, point):
        checkpoint = self.checkPoint[self.i_checkPoint]

        if polar.dist(point, checkpoint) < 20:
            self.i_checkPoint = (self.i_checkPoint + 1) % len(self.checkPoint)
            print("Checkpoint preso!")
