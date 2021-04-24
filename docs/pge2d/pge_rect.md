Use the Class Rect to create a Rect on the screen

```py
import pge2d as pge

class my_game(pge.game):
    player = pge.rect()
    def update():
        self.player.draw()

my_game()
```

Parans:
- position: (0, 0) # X and Y
- color: (0, 0, 0) # RGB Color or pge.color.color_name()
- size: (50, 50) # Width and Height

Handling Class Variables:

- rect.x: rect x
- rect.y: rect y
- rect.color: rect color
- rect.height: rect height
- rect.width: rect width

Use function draw() in Game Update() to draw this object

[Return 2D-Docs](README.md)
