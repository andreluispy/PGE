# PGE
 Python Game Engine make with PyGame

 An easier alternative that automates the things you would do with PyGame

# Starting
 Install with pip in windows:
 `pip install pge-engine`
 
 Install with pip3 in Linux Ubuntu:
 `pip3 install pge-engine`

## Creating a simple game!
 To start first import PGE Game Engine and create a class that will receive the type pge.game:
 ```py
import pge

class mygame(pge.game):
    def start(self):
        pass
    def update(self):
        pass

mygame()
 ```

 The func start is call on game start and fun update is call in loop.

 Creating a circle, the circle is created within the class of our game and then we need inside the update function to call the circle in the draw function and passing our display as an argument just by passing: `self.display`

 ```py
import pge

class mygame(pge.game):
    '''
    Player color is green in rgb, it is possible for the color of the player to be pge.green or pge.lime
    '''

    player = pge.circle(position=(0, 0), color=(0, 255, 0))

    def start(self):
        pass
    def update(self):
        self.player.draw(self.display)

mygame()
 ```

 Capturing inputs and move player

 ```py
import pge

class mygame(pge.game):
    player = pge.circle(position=(0, 0), color=(0, 255, 0))

    def start(self):
        pass
    def update(self):
        self.player.draw(self.display)

        if pge.key.get_key_pressed('s') == True:
            self.player.y += 10
        if pge.key.get_key_pressed('w') == True:
            self.player.y -= 10
        if pge.key.get_key_pressed('d') == True:
            self.player.x += 10
        if pge.key.get_key_pressed('a') == True:
            self.player.x -= 10

mygame()
 ```
