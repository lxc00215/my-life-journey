import pygame as pg
import math
import struct
import io

def _get_chinese_font(size):
    """Get a font that supports Chinese characters"""
    font_names = ['simhei', 'microsoftyahei', 'simsun', 'stheiti', 
                  'wenquanyimicrohei', 'notosanscjksc', 'droidsansfallback',
                  'arial']
    for name in font_names:
        try:
            font = pg.font.SysFont(name, size)
            # Test if it can render Chinese
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

def create_fireworks_sound():
    """Generate a simple fireworks explosion sound"""
    sample_rate = 22050
    duration = 0.4
    num_samples = int(sample_rate * duration)
    
    buf = io.BytesIO()
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', 36 + num_samples * 2))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<IHHIIHH', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16))
    buf.write(b'data')
    buf.write(struct.pack('<I', num_samples * 2))
    
    for i in range(num_samples):
        t = i / sample_rate
        progress = t / duration
        freq = 800 * (1 - progress) + 200
        amp = int(16000 * (1 - progress) * (1 - progress))
        sample = int(amp * math.sin(2 * math.pi * freq * t))
        sample = max(-32768, min(32767, sample))
        buf.write(struct.pack('<h', sample))
    
    buf.seek(0)
    sound = pg.mixer.Sound(buf)
    return sound

def create_jump_sound():
    """Generate a jump sound"""
    sample_rate = 22050
    duration = 0.15
    num_samples = int(sample_rate * duration)
    
    buf = io.BytesIO()
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', 36 + num_samples * 2))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<IHHIIHH', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16))
    buf.write(b'data')
    buf.write(struct.pack('<I', num_samples * 2))
    
    for i in range(num_samples):
        t = i / sample_rate
        progress = t / duration
        freq = 300 + 400 * progress
        amp = int(12000 * (1 - progress))
        sample = int(amp * math.sin(2 * math.pi * freq * t))
        sample = max(-32768, min(32767, sample))
        buf.write(struct.pack('<h', sample))
    
    buf.seek(0)
    sound = pg.mixer.Sound(buf)
    return sound

def create_powerup_sound():
    """Generate a powerup collect sound"""
    sample_rate = 22050
    duration = 0.3
    num_samples = int(sample_rate * duration)
    
    buf = io.BytesIO()
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', 36 + num_samples * 2))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<IHHIIHH', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16))
    buf.write(b'data')
    buf.write(struct.pack('<I', num_samples * 2))
    
    for i in range(num_samples):
        t = i / sample_rate
        progress = t / duration
        freq = 400 + 600 * progress
        amp = int(14000 * (1 - progress * 0.5))
        sample = int(amp * math.sin(2 * math.pi * freq * t))
        sample = max(-32768, min(32767, sample))
        buf.write(struct.pack('<h', sample))
    
    buf.seek(0)
    sound = pg.mixer.Sound(buf)
    return sound

def create_flag_sound():
    """Generate a flag pole slide sound"""
    sample_rate = 22050
    duration = 0.6
    num_samples = int(sample_rate * duration)
    
    buf = io.BytesIO()
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', 36 + num_samples * 2))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<IHHIIHH', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16))
    buf.write(b'data')
    buf.write(struct.pack('<I', num_samples * 2))
    
    for i in range(num_samples):
        t = i / sample_rate
        progress = t / duration
        freq = 600 - 300 * progress
        amp = int(15000 * (1 - progress * 0.3))
        sample = int(amp * math.sin(2 * math.pi * freq * t))
        sample = max(-32768, min(32767, sample))
        buf.write(struct.pack('<h', sample))
    
    buf.seek(0)
    sound = pg.mixer.Sound(buf)
    return sound

def create_level_complete_sound():
    """Generate a level complete sound"""
    sample_rate = 22050
    duration = 1.2
    num_samples = int(sample_rate * duration)
    
    buf = io.BytesIO()
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', 36 + num_samples * 2))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<IHHIIHH', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16))
    buf.write(b'data')
    buf.write(struct.pack('<I', num_samples * 2))
    
    notes = [523, 659, 784, 1047]
    note_duration = duration / len(notes)
    
    for i in range(num_samples):
        t = i / sample_rate
        note_index = min(int(t / note_duration), len(notes) - 1)
        freq = notes[note_index]
        progress = (t % note_duration) / note_duration
        amp = int(14000 * (1 - progress * 0.3))
        sample = int(amp * math.sin(2 * math.pi * freq * t))
        sample = max(-32768, min(32767, sample))
        buf.write(struct.pack('<h', sample))
    
    buf.seek(0)
    sound = pg.mixer.Sound(buf)
    return sound

def create_death_sound():
    """Generate a death sound"""
    sample_rate = 22050
    duration = 0.8
    num_samples = int(sample_rate * duration)
    
    buf = io.BytesIO()
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', 36 + num_samples * 2))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<IHHIIHH', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16))
    buf.write(b'data')
    buf.write(struct.pack('<I', num_samples * 2))
    
    for i in range(num_samples):
        t = i / sample_rate
        progress = t / duration
        freq = 600 - 400 * progress
        amp = int(14000 * (1 - progress))
        sample = int(amp * math.sin(2 * math.pi * freq * t))
        sample = max(-32768, min(32767, sample))
        buf.write(struct.pack('<h', sample))
    
    buf.seek(0)
    sound = pg.mixer.Sound(buf)
    return sound

def create_fireball_sound():
    """Generate a fireball sound"""
    sample_rate = 22050
    duration = 0.12
    num_samples = int(sample_rate * duration)
    
    buf = io.BytesIO()
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', 36 + num_samples * 2))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<IHHIIHH', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16))
    buf.write(b'data')
    buf.write(struct.pack('<I', num_samples * 2))
    
    for i in range(num_samples):
        t = i / sample_rate
        progress = t / duration
        freq = 1000 - 600 * progress
        amp = int(10000 * (1 - progress))
        sample = int(amp * math.sin(2 * math.pi * freq * t))
        sample = max(-32768, min(32767, sample))
        buf.write(struct.pack('<h', sample))
    
    buf.seek(0)
    sound = pg.mixer.Sound(buf)
    return sound

def create_stomp_sound():
    """Generate a stomp/enemy kill sound"""
    sample_rate = 22050
    duration = 0.15
    num_samples = int(sample_rate * duration)
    
    buf = io.BytesIO()
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', 36 + num_samples * 2))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<IHHIIHH', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16))
    buf.write(b'data')
    buf.write(struct.pack('<I', num_samples * 2))
    
    for i in range(num_samples):
        t = i / sample_rate
        progress = t / duration
        freq = 400 - 200 * progress
        amp = int(12000 * (1 - progress))
        sample = int(amp * math.sin(2 * math.pi * freq * t))
        sample = max(-32768, min(32767, sample))
        buf.write(struct.pack('<h', sample))
    
    buf.seek(0)
    sound = pg.mixer.Sound(buf)
    return sound


class SoundManager:
    """Manages all game sounds"""
    def __init__(self):
        self.sounds = {}
        self.enabled = True
        self._init_sounds()
    
    def _init_sounds(self):
        try:
            pg.mixer.init()
            self.sounds['jump'] = create_jump_sound()
            self.sounds['powerup'] = create_powerup_sound()
            self.sounds['flag'] = create_flag_sound()
            self.sounds['level_complete'] = create_level_complete_sound()
            self.sounds['death'] = create_death_sound()
            self.sounds['fireball'] = create_fireball_sound()
            self.sounds['fireworks'] = create_fireworks_sound()
            self.sounds['stomp'] = create_stomp_sound()
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
