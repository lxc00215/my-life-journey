import pygame as pg


def _get_chinese_font(size):
    font_names = ['simhei', 'microsoftyahei', 'simsun', 'stheiti',
                  'wenquanyimicrohei', 'notosanscjksc', 'droidsansfallback',
                  'arial']
    for name in font_names:
        try:
            font = pg.font.SysFont(name, size)
            test = font.render('测', True, (255,255,255))
            if test.get_width() > 5:
                return font
        except:
            continue
    return pg.font.Font(None, size)


def create_pixel_text(text, font_size=10, color=(255, 255, 255), bg_color=None, scale=2):
    font = _get_chinese_font(font_size)
    if bg_color:
        small_surface = font.render(text, False, color, bg_color)
    else:
        small_surface = font.render(text, False, color)
    small_rect = small_surface.get_rect()
    scaled_surface = pg.transform.scale(small_surface,
        (small_rect.width * scale, small_rect.height * scale))
    return scaled_surface


def create_pixel_text_with_border(text, font_size=10, text_color=(255, 255, 255),
                                   bg_color=(0, 0, 0), border_color=(255, 255, 255),
                                   scale=2, padding=2):
    font = _get_chinese_font(font_size)
    small_surface = font.render(text, False, text_color, bg_color)
    small_rect = small_surface.get_rect()

    total_w = small_rect.width + padding * 2
    total_h = small_rect.height + padding * 2

    bg_surface = pg.Surface((total_w, total_h))
    bg_surface.fill(border_color)
    inner_rect = pg.Rect(padding - 1, padding - 1,
                         small_rect.width + 1, small_rect.height + 1)
    pg.draw.rect(bg_surface, bg_color, inner_rect)
    bg_surface.blit(small_surface, (padding, padding))

    scaled_surface = pg.transform.scale(bg_surface,
        (total_w * scale, total_h * scale))
    return scaled_surface


class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.enabled = True
        self.current_music = None
        self._init_sounds()
    
    def _init_sounds(self):
        try:
            pg.mixer.init()
            from .. import setup
            sfx_map = {
                'small_jump': 'small_jump',
                'big_jump': 'big_jump',
                'jump': 'small_jump',
                'powerup': 'powerup',
                'powerup_appears': 'powerup_appears',
                'flag': 'flagpole',
                'level_complete': 'stage_clear',
                'death': 'death',
                'fireball': 'fireball',
                'fireworks': 'coin',
                'stomp': 'stomp',
                'coin': 'coin',
                'kick': 'kick',
                'bump': 'bump',
                'brick_smash': 'brick_smash',
                'one_up': 'one_up',
                'pipe': 'pipe',
                'count_down': 'out_of_time',
                'game_over': 'game_over',
                'invincible': 'invincible',
            }
            for key, sfx_name in sfx_map.items():
                if sfx_name in setup.SFX:
                    self.sounds[key] = setup.SFX[sfx_name]
        except Exception as e:
            print(f"Sound init failed: {e}")
            self.enabled = False
    
    def play(self, name, volume=0.5):
        if self.enabled and name in self.sounds:
            try:
                self.sounds[name].set_volume(volume)
                self.sounds[name].play()
            except:
                pass
    
    def play_music(self, name, volume=0.4, loops=-1):
        if self.enabled:
            try:
                from .. import setup
                if name in setup.MUSIC:
                    pg.mixer.music.load(setup.MUSIC[name])
                    pg.mixer.music.set_volume(volume)
                    pg.mixer.music.play(loops)
                    self.current_music = name
            except Exception as e:
                print(f"Music play failed: {e}")
    
    def stop_music(self):
        try:
            pg.mixer.music.stop()
            self.current_music = None
        except:
            pass
