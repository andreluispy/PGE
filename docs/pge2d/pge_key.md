Use this module to manipule keyboard events

Functions:
- get_key_pressed(key: str): Check if a key has been pressed, type of keys to pass:

        Types of Key:
            q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, esc, up, down, left, right, left_shift, right_shift, left_ctrl, right_ctrl, left_alt, right_alt, enter, tab, capslock, space, backspace, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, delete

```py
import pge2d as pge

class my_game(pge.game):
    def update(self):
        if pge.key.get_key_pressed('space'):
            print('Space key has pressed')

my_game()
```

[Return 2D-DOCS](README.md)
