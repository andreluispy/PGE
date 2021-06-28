import pge2d as pge
from random import randint

class my_game(pge.game):
    player = pge.sprite(position=(400, 10), img='data/player.png', size=(32, 32))
    #player = pge.rect(position=(400, 10), color=pge.color.blue(), size=(30, 30))
    point = pge.circle(position=(400, 300), color=pge.color.lime(), radius=10)

    def start(self):
        self.window_title = 'My Game'
        self.window_color = pge.color.deep_sky_blue()
        pge.mixer.music.play('data/music.wav', 'loop')
        pge.mixer.music.set_volume(0.3)

    def update(self):
        self.point.draw()
        self.player.draw()

        if pge.collision(self.player, self.point):
            self.point.x, self.point.y = (randint(0,800), randint(0, 600))
            pge.mixer.sound.play(music='data/coin.wav')

        # Quit Event
        if pge.key.get_key_pressed('esc'):
            pge.quit()
        
        # Motion(Mouse)
        if pge.mouse.left_pressed():
            if pge.mouse.x > self.player.x:
                self.player.x += 10
                self.player.flip_horizontal = False
            if pge.mouse.x < self.player.x:
                self.player.x -= 10
                self.player.flip_horizontal = True
            if pge.mouse.y > self.player.y:
                self.player.y += 10
            if pge.mouse.y < self.player.y:
                self.player.y -= 10
        
        # Motion(keyboard)
        if pge.key.get_key_pressed('w'):
            self.player.y -= 10
        if pge.key.get_key_pressed('s'):
            self.player.y += 10
        if pge.key.get_key_pressed('a'):
            self.player.x -= 10
            self.player.flip_horizontal = True
        if pge.key.get_key_pressed('d'):
            self.player.x += 10
            self.player.flip_horizontal = False

my_game()
