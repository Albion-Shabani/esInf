from lib.polar import move_around

def clamp(v, vmin, vmax):
    return min(max(v, vmin), vmax)

class Car:
    def __init__(self, pos):
        self._x, self._y = pos
        self._speed = 0
        self._angle = 0            # in passi di rotazione (0..31)
        self._rot = 90 / 8         # gradi per passo
        self._max_speed = 8

    def move(self, keys):
        if "ArrowRight" in keys and "ArrowLeft" not in keys:
            self._angle += 1
            self._speed -= 0.6
        if "ArrowLeft" in keys and "ArrowRight" not in keys:
            self._angle -= 1
            self._speed -= 0.6
        self._angle %= 32

        # velocità
        if "ArrowUp" in keys:
            self._speed += 0.3      # accelera
        elif "ArrowDown" in keys:
            self._speed -= 0.6      # frena
        else:
            self._speed -= 0.15     # attrito

        self._speed = clamp(self._speed, 0, self._max_speed)

        self._x, self._y = move_around((self._x, self._y),self._speed,self._angle * self._rot)

    def pos(self):
        return self._x, self._y

    def newPos(self,point):
        print(point)
        self._x, self._y = point

    def sprite(self):
        sprite_y, sprite_x = divmod(-self._angle % 32, 8)
        #sprite_x += 8
        #sprite_y += 4
        return (sprite_x * 16, sprite_y * 16, 16, 16)