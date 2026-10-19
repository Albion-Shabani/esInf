#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Ball:
    def __init__(self,home):
        self._x = home[0]
        self._y = home[1]
        self.home = home
        self._dx, self._dy = random.randint(-10, 10),random.randint(-10, 10)

    def move(self):
        if self._x + self._dx > ARENA_W or self._x + self._dx < 0 or self._y + self._dy > ARENA_H or self._y + self._dy < 0:
            self._x = self.home[0]
            self._dx = random.randint(-10, 10)
            self._y = self.home[1]
            self._dy = random.randint(-10, 10)
        self._x += self._dx
        self._y += self._dy
        
    def pos(self) -> tuple[int, int]:
        return self._x, self._y


def tick():
    g2d.clear_canvas()  # BG
    g2d.draw_image("ball.png", b1.pos())  # FG
    g2d.draw_image("ball.png", b2.pos())
    b1.move()
    b2.move()


def main():
    global b1,b2, g2d,random
    import g2d,random  # Ball does not depend on g2d
    home1 = (10,20)
    home2 = (100,300)
    b1 = Ball(home1)
    b2 = Ball(home2)


    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
