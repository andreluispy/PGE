Use the collision module to detect collisions between 2 objects

```py
import pge2d as pge

class my_game(pge.game):
    player = pge.circle(position=(400, 10), color=pge.color.lime(), radius=50)

    point = pge.circle(position=(400, 300), color=pge.color.red())

    def start(self):
        self.score = 0

    def update(self):
        if pge.collision(self.player, self.point):
            self.score += 1

my_game()
```

 This is a comand to simplifique rect collision

[Return 2D-DOCS](README.md)
