The Class text is used to create a text in your game

To use it, create a object:

```py
import pge2d as pge

class my_game(pge.game):
    text = pge.text()

    def update(self):
        self.text.draw()

my_game()

```

Use function draw() in Game Update() to draw this objects, pass parans in draw() function.

Parans:
- text: "My Text"  # The text
- font: "Arial"    # font of text
- font_size: 10    # size of text
- position: (0, 0) # X and Y
- color: (0, 0, 0) # RGB
- bold: False
- italic: False
- antialias: False # if True the characters will have smooth edges
- background: None # RGB

[Return 2D-Docs](README.md)
