import pygame as pg


class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.enabled = True
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
                'flag': 'pipe',
                'level_complete': 'main_theme_sped_up',
                'death': 'pipe',
                'fireball': 'fireball',
                'fireworks': 'coin',
                'stomp': 'stomp',
                'coin': 'coin',
                'kick': 'kick',
                'bump': 'bump',
                'brick_smash': 'brick_smash',
                'one_up': 'one_up',
                'pipe': 'pipe',
                'count_down': 'count_down',
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
