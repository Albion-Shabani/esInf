import lib.g2d as g2d
import car
import arena


car1 = car.Car((100, 100))
_arena = arena.Arena()

def tick():
    g2d.clear_canvas()
    _arena.draw_map()
    car1.move(g2d.current_keys())
    x,y = car1.pos()
    
    if not _arena.is_road(x,y):
        print("muro")

    sx, sy, sw, sh = car1.sprite()
    g2d.draw_image("super-sprint.png", car1.pos(), (sx, sy), (sw, sh))

g2d.init_canvas((_arena.MAP_W, _arena.VIEW_H), _arena.SCALE)
g2d.main_loop(tick)