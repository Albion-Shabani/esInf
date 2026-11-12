import lib.polar as polar

def clamp(v, vmin, vmax):
    return min(max(v, vmin), vmax)

WAYPOINTS = [
    (216.0, 64.0), (375.0, 65.0), (441.0, 160.0), (437.0, 266.0), 
    (412.0, 316.0), (341.0, 339.0), (260.0, 224.0), (170.0, 222.0),
      (149.0, 332.0), (85.0, 313.0), (73.0, 231.0), (66.0, 128.0), 
      (97.0, 66.0)
    ]

class Opponent:
    def __init__(self):
        self._wps = WAYPOINTS
        self._i = 1                       # prossimo waypoint da raggiungere
        self._x, self._y = WAYPOINTS[0]   # parte dal primo punto (centro)
        self._speed = 0
        self._angle = 0
        self._rot = 90 / 8         # gradi per passo
        self._max_speed = 6

    def move(self):
        target = self._wps[self._i]
        pos = (self._x, self._y)

        if polar.dist(pos,target) < 15:
            self._i = (self._i + 1) % len(self._wps)
            target = self._wps[self._i]

        _, want = polar.to_polar(polar.vector(pos, target))             #angolo per andare al target
        diff = polar.coterminal(want - self._angle * self._rot)

        if diff > self._rot:
            self._angle += 1
        elif diff < -self._rot:
            self._angle -= 1

        if abs(diff) < 60:
            self._speed += 0.2
        else:
            self._speed -= 0.4

        self._speed = clamp(self._speed, 0, self._max_speed)
        self._x, self._y = polar.move_around(pos, self._speed,self._angle * self._rot)
            
    def pos(self):
        return self._x, self._y
    
    def sprite(self):
        sprite_y, sprite_x = divmod(-self._angle % 32, 8)
        sprite_y += 4           # macchina rossa
        return (sprite_x * 16, sprite_y * 16, 16, 16)

import lib.g2d as g2d
import arena


