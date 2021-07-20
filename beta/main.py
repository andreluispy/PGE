import pge2d as pge
from random import randint

class game(pge.game):
    window_title = 'Game'
    window_color = (0, 255, 0)

    # vars
    score = 0

    # objects
    player = pge.sprite((400, 10), 'data/player.png')
    fruit = pge.circle((400, 300), pge.color.red(), 10)

    # UI
    score_text = pge.text()

    def start(self):
        pge.mixer.music.play("data/music.wav", 'loop')
        pge.mixer.music.set_volume(0.2)
    def update(self):
        self.player.draw()
        self.fruit.draw()
        self.score_text.draw(f'Score: {self.score}', font_size=30, position=(10, 10), bold=True)

        if pge.key.get_key_pressed("w"):
            self.player.y -= 10
        if pge.key.get_key_pressed("s"):
            self.player.y += 10
        if pge.key.get_key_pressed("a"):
            self.player.x -= 10
            self.player.flip_horizontal = True
        if pge.key.get_key_pressed("d"):
            self.player.x += 10
            self.player.flip_horizontal = False
        
        if pge.collision(self.player, self.fruit):
            self.fruit.x = randint(10, 790)
            self.fruit.y = randint(10, 590)
            self.score += 1
            pge.mixer.sound.play("data/coin.wav", volume=1)

game()
