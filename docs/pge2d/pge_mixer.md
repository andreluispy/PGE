Class to manage game sounds

Functions:
- mixer.music:
    - play(music, repeat, start, fade): use to play a music, parans:
        - music: Str with music archive
        - repeat: Music repeat num with INT num
        - start: Float num, music time to start
        - fade: int num, fade of music
        
        To loop: play music in function start and pass to repeat: "loop"
    - pause(): Use to pause music
    - unpause(): Use to unpause music
    - restart(): Use to restart music
    - stop(): Use to stop music
    - set_volume(volume: float): Use to set music volume, volume is a num between 0-1
    - get_volume(): Get music volume
    - sound_length(): Get music length
- mixer.sound:
    - play(music: str, volume: float): Play a game sound

[Return 2D-DOCS](README.md)