__author__ = 'marble_xu'

import os
import pygame as pg
from . import constants as c
from . import tools

pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

GFX = tools.load_all_gfx(os.path.join("resources","graphics"))

SFX = {}
def load_all_sfx(directory, accept=('.ogg', '.wav', '.mp3')):
    for name in os.listdir(directory):
        if os.path.splitext(name)[1].lower() in accept:
            filepath = os.path.join(directory, name)
            sfx_name = os.path.splitext(name)[0]
            try:
                SFX[sfx_name] = pg.mixer.Sound(filepath)
            except Exception as e:
                print(f"Failed to load sound {filepath}: {e}")

sound_dir = os.path.join("resources", "sound")
if os.path.exists(sound_dir):
    load_all_sfx(sound_dir)

MUSIC = {}
music_dir = os.path.join("resources", "music")
if os.path.exists(music_dir):
    for name in os.listdir(music_dir):
        if os.path.splitext(name)[1].lower() in ('.ogg', '.wav', '.mp3'):
            filepath = os.path.join(music_dir, name)
            music_name = os.path.splitext(name)[0]
            try:
                MUSIC[music_name] = filepath
            except Exception as e:
                print(f"Failed to load music {filepath}: {e}")