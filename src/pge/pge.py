import pygame
from sys import exit

class game:
    # Window Configs
    display = pygame.Surface

    window_size = (800, 600)
    window_title = 'Game'
    window_color = (0, 0, 0)

    def __init__(self):
        # window render
        pygame.init()
        self.display = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)

        print('\n')
        self.start()

        while True:
            # Engine components
            mouse.x, mouse.y = pygame.mouse.get_pos()

            # PyGame Engine
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display.fill(self.window_color)

            self.update()

            pygame.display.update()

    def start(self):
        pass
    def update(self):
        pass

def quit():
    pygame.quit()
    exit()

class circle:
    '''
    parans:
        position: (0, 0) # X and Y
        color: (0, 0, 0) # RGB
        radius: 1        # Circle Radius
    '''
    x = 0
    y = 0
    color = (0, 0, 0)
    radius = 50

    def __init__(self, position: tuple, color: tuple, radius):
        self.x, self.y = position
        self.color = color
        self.radius = radius

    def draw(self, window):
        '''
        parans:
            window: # Please insert "self.display"
        '''
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

class rect:
    '''
    parans:
        position: (0, 0) # X and Y
        color: (0, 0, 0) # RGB
        size: (50, 50)   # Width and Height
    '''
    x = 0
    y = 0
    height = 1
    width = 1
    color = (0, 0, 0)

    def __init__(self, position: tuple, size: tuple, color: tuple):
        self.x, self.y = position
        self.width, self.height = size
        self.color = color

    def draw(self, window):
        '''
        parans:
            window: # Please insert "self.display"
        '''
        self.square = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.color, rect=self.square)
        pass

class sprite:
    '''
    parans:
        position: (0, 0)  # X and Y
        size: (0, 0)      # width and height, (0, 0) to img standard size
        img: 'player.png' # Img to Draw
    '''
    x = 0
    y = 0
    height = 0
    width = 0
    img = ''
    flip_horizontal = False
    flip_vertical = False

    def __init__(self, position, img, size=(0, 0)):
        self.x, self.y = position
        self.width, self.height = size
        self.img = img

    def draw(self, window):
        '''
        parans:
            window: # Please insert "self.display"
        '''
        if self.width == 0 or self.height == 0:
            sprite = pygame.transform.flip(pygame.image.load(self.img), self.flip_horizontal, self.flip_vertical)
        else:
            sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.img), [self.height, self.width]), self.flip_horizontal, self.flip_vertical)

        window.blit(sprite, (self.x, self.y))

class key:
    def get_key_pressed(key: str):
        '''
        Parans: key: str

        |

        Types of Key:
            q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, esc, up, down, left, right, left_shift, right_shift, left_ctrl, right_ctrl, left_alt, right_alt, enter, tab, capslock, space, backspace, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, delete
        '''
        # keymap
        keymap = {'q':pygame.K_q, 'w':pygame.K_w, 'e':pygame.K_e, 'r':pygame.K_r, 't':pygame.K_t, 'y':pygame.K_y, 'u':pygame.K_u, 'i':pygame.K_i, 'o':pygame.K_o, 'p':pygame.K_p, 'a':pygame.K_a, 's':pygame.K_s, 'd':pygame.K_d, 'f':pygame.K_f, 'g':pygame.K_g, 'h':pygame.K_h, 'j':pygame.K_j, 'k':pygame.K_k, 'l':pygame.K_l, 'z':pygame.K_z, 'x':pygame.K_x, 'c':pygame.K_c, 'v': pygame.K_v, 'b':pygame.K_b, 'n':pygame.K_n, 'm':pygame.K_m, '1':pygame.K_1, '2':pygame.K_2, '3':pygame.K_3, '4':pygame.K_4, '5':pygame.K_5, '6':pygame.K_6, '7':pygame.K_7, '8':pygame.K_8, '9':pygame.K_9, '0':pygame.K_0, 'esc':pygame.K_ESCAPE, 'up':pygame.K_UP, 'down':pygame.K_DOWN, 'left':pygame.K_LEFT, 'right':pygame.K_RIGHT, 'left_shift':pygame.K_LSHIFT, 'right_shift':pygame.K_RSHIFT, 'left_ctrl':pygame.K_LCTRL, 'right_ctrl':pygame.K_RCTRL, 'left_alt':pygame.K_LALT, 'right_alt':pygame.K_RALT, 'enter':pygame.K_RETURN, 'tab':pygame.K_TAB, 'capslock':pygame.K_CAPSLOCK, 'space':pygame.K_SPACE, 'backspace':pygame.K_BACKSPACE, 'f1':pygame.K_F1, 'f2':pygame.K_F2, 'f3':pygame.K_F3, 'f4':pygame.K_F4, 'f5':pygame.K_F5, 'f6':pygame.K_F6, 'f7':pygame.K_F7, 'f8':pygame.K_F8, 'f9':pygame.K_F9, 'f10':pygame.K_F10, 'f11':pygame.K_F11, 'f12':pygame.K_F12, 'delete':pygame.K_DELETE}

        if pygame.key.get_pressed()[keymap[key.lower()]] == True:
            return True

class mouse:
    x, y = 0, 0

    # Set Atributs
    def set_visible(visible: bool):
        pygame.mouse.set_visible(visible)
    def set_position(position: tuple):
        mx, my = position
        pygame.mouse.set_pos([mx, my])

    # Get Atributs
    def get_visible():
        return pygame.mouse.get_visible()

    # Get presseds
    def left_pressed():
        if pygame.mouse.get_pressed()[0]:
            return True
    def right_pressed():
        if pygame.mouse.get_pressed()[2]:
            return True
    def middle_pressed():
        if pygame.mouse.get_pressed()[0]:
            return True
    def get_pressed(button: int):
        if pygame.mouse.get_pressed()[button]:
            return True
    def overlapping_obj(obj):
        if mouse.x > obj.x and mouse.x < obj.x+obj.width and mouse.y > obj.y and mouse.y < obj.y+obj.height:
            return True

class color:
    def black():
        return (0, 0, 0)
    def white():
        return (255, 255, 255)
    def red():
        return (255, 0, 0)
    def blue():
        return (0, 0, 255)
    def green():
        return (0,128,0)
    def yellow():
        return (255, 255, 0)
    def magenta():
        return (255, 0, 255)
    def cyan():
        return (0, 255, 255)
    def silver():
        return (192, 192, 192)
    def gray():
        return (128, 128, 128)
    def purple():
        return (128, 0, 128)
    def orange():
        return (255,165,0)
    def gold():
        return (255,215,0)
    def lime():
        return (0,255,0)
    def dark_green():
        return (0,100,0)
    def turquoise():
        return (64,224,208)
    def aqua_marine():
        return (127,255,212)
    def deep_sky_blue():
        return (0,191,255)
    def violet():
        return (238,130,238)
    def dark_violet():
        return (148,0,211)
    def pink():
        return (255,192,203)
    def brow():
        return (139,69,19)
