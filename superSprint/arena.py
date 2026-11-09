import lib.g2d as g2d

class Arena():
    def __init__(self):
        self.MAP_W, self.MAP_H = 512, 480
        self.BAR = 64                  # altezza della striscia nera in alto
        self.VIEW_H = self.MAP_H - self.BAR      # 416
        self.SCALE = 2.5
        self.BG = g2d.load_image("super-sprint-bg.png")
        self.bg_surf = g2d._loaded[self.BG]          # la Surface di pygame caricata da g2d

    def draw_map(self):
        g2d.draw_image("super-sprint-bg.png", (0, 0), (0, self.BAR), (self.MAP_W, self.VIEW_H))

    def is_road(self,x, y):
        """True se il pixel (x, y) del canvas è asfalto."""
        x, y = int(x), int(y)
        if not (0 <= x < self.MAP_W and 0 <= y < self.VIEW_H):
            return False
        r, g, b = self.bg_surf.get_at((x, y + self.BAR))[:3]   # + BAR: salto la striscia nera
        return r == g == b and 80 <= r <= 200  

