## Creating a simple game!
 To start first import PGE Game Engine and create a class that will receive the type pge.game:
 ```py
import pge2d as pge

class mygame(pge.game):
    def start(self):
        pass
    def update(self):
        pass

mygame()
 ```

 The func start is call on game start and fun update is call in loop.

 Creating a circle, the circle is created within the class of our game and then we need inside the update function to call the circle in the draw function

 ```py
import pge2d as pge

class mygame(pge.game):
    '''
    Player color is green in rgb, it is possible for the color of the player to be pge.color.green() or pge.color.lime()
    '''

    player = pge.circle(position=(0, 0), color=(0, 255, 0))

    def start(self):
        pass
    def update(self):
        self.player.draw()

mygame()
 ```

 Capturing inputs and move player

 ```py
import pge2d as pge

class mygame(pge.game):
    player = pge.circle(position=(0, 0), color=(0, 255, 0))

    def start(self):
        pass
    def update(self):
        self.player.draw()

        if pge.key.get_key_pressed('s'):
            self.player.y += 10
        if pge.key.get_key_pressed('w'):
            self.player.y -= 10
        if pge.key.get_key_pressed('d'):
            self.player.x += 10
        if pge.key.get_key_pressed('a'):
            self.player.x -= 10

mygame()
 ```

# Pge2D Modules
 See Pge modules and their functions:

 - [pge.game](pge_game.md)
 - [pge.quit](pge_quit.md)
 - [pge.circle](pge_circle.md)
 - [pge.rect](pge_rect.md)
 - [pge.sprite](pge_sprite.md)
 - [pge.collision](pge_collision.md)
 - [pge.key](pge_key.md)
 - [pge.mouse](pge_mouse.md)
 - [pge.color](pge_color.md)
 - [pge.mixer](pge_mixer.md)

[Return to Docs Main](../README.md)
