Use the Class Circle to create a circle on the screen

```py
import pge2d as pge

class my_game(pge.game):
    player = pge.circle()
    def update():
        self.player.draw()

my_game()
```

Parans:
- position: (0, 0) # X and Y
- color: (0, 0, 0) # RGB Color or pge.color.color_name()
- Radius: Int or Float # Circle size

Handling Class Variables:

- circle.x: Circle X
- circle.y: Circle Y
- circle.color: Circle Color
- circle.radius: Circle Radius
- circle.width: Circle Width
- circle.height: Circle Height

Use function draw() in Game Update() to draw this object

[Return 2D-Docs](README.md)
