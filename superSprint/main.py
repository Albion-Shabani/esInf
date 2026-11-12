import lib.g2d as g2d
import car,arena,oppenet

car1 = car.Car((100, 100))
oppenet1 = oppenet.Opponent()
_arena = arena.Arena()

def tick():
    g2d.clear_canvas()
    _arena.draw_map()
    _arena.draw_checkPoint()

    car1.move(g2d.current_keys())
    oppenet1.move()

    x,y = car1.pos()
    
    sx, sy, sw, sh = car1.sprite()
    g2d.draw_image("super-sprint.png", car1.pos(), (sx, sy), (sw, sh))

    ox,oy,ow,oh = oppenet1.sprite()
    g2d.draw_image("super-sprint.png", oppenet1.pos(), (ox, oy), (ow, oh))

    _arena.check_checkPoint(car1.pos())
    if not _arena.is_road(x,y):
        car1.newPos(_arena.get_checkPoint())        #checkpoint

g2d.init_canvas((_arena.MAP_W, _arena.VIEW_H), _arena.SCALE)
g2d.main_loop(tick)