Use the Class sprite to create a sprite on the screen

```py
import pge2d as pge

class my_game(pge.game):
    player = pge.sprite()
    def update():
        self.player.draw()

my_game()
```

Parans:
- position: (0, 0) # X and Y
- img: `'data/player.png'` # Player Sprite Location
- size: (32, 32) # Rezise the sprite, insert nothing to standart img size

Handling Class Variables:

- sprite.x: sprite x
- sprite.y: sprite y
- sprite.height: sprite height
- sprite.width: sprite width
- sprite.img: sprite image

Fliping a image:

- sprite.flip_horizontal = bool
- sprite.flip_vertical = bool

Use function draw() in Game Update() to draw this object

[Return 2D-Docs](README.md)
