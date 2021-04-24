The Class Game is used to create a display where you can create your game

To use it, create a class that inherits it:

```py
import pge2d as pge

class my_game(pge.game):
    pass

my_game()

```

Within this class you can create your objects that will be called in the update function

The class will have 2 functions, update and start:

-start: The function called at the beginning of your game, here you declare things like songs that will be looped and events that are only called once

-update: The loop where your game takes place, in it you call the draw () function of your objects and program the events that are always called

Note that you should not overwrite the class init function, this breaks the engine system

```py
import pge2d as pge

class my_game(pge.game):
    def start(self):
        pass
    def update(self):
        pass

my_game()
```

[Return 2D-Docs](README.md)
