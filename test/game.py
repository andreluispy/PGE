import pge

class joguinho(pge.game):
    window_color = (0, 0, 255)

    player = pge.sprite(position=(400, 10), size=(128, 128), img='player.png')

    def update(self):
        self.player.draw(self.display)

        # Mouse click in player and position reset
        if pge.mouse.left_pressed() == True:
            if pge.mouse.overlapping_obj(self.player) == True:
                self.player.x = 400
                self.player.y = 10

        # Player move(mouse)
        if pge.mouse.left_pressed() == True:
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

        # Player move(keyboard)
        if pge.key.get_key_pressed('s') == True:
            self.player.y += 10
        if pge.key.get_key_pressed('w') == True:
            self.player.y -= 10
        if pge.key.get_key_pressed('d') == True:
            self.player.x += 10
            self.player.flip_horizontal = False
        if pge.key.get_key_pressed('a') == True:
            self.player.x -= 10
            self.player.flip_horizontal = True

joguinho()
