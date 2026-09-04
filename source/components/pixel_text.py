import pygame as pg

def create_pixel_text(text, font_size=8, color=(255, 255, 255), bg_color=None, scale=3):
    """
    Create a pixel-style text surface.
    Renders at small font size then scales up for pixel art look.
    
    Args:
        text: string to render
        font_size: base font size (small = more pixelated)
        color: text color RGB tuple
        bg_color: background color RGB tuple, or None for transparent
        scale: scale factor for upscaling
    
    Returns:
        pygame.Surface with the rendered text
    """
    try:
        font = pg.font.SysFont('consolas', font_size)
    except:
        font = pg.font.Font(None, font_size)
    
    # Render at small size
    if bg_color:
        small_surface = font.render(text, False, color, bg_color)
    else:
        small_surface = font.render(text, False, color)
    
    # Scale up with nearest neighbor for pixel look
    small_rect = small_surface.get_rect()
    scaled_surface = pg.transform.scale(small_surface,
        (small_rect.width * scale, small_rect.height * scale))
    
    return scaled_surface

def create_pixel_text_with_border(text, font_size=8, text_color=(255, 255, 255), 
                                   bg_color=(0, 0, 0), border_color=(255, 255, 255),
                                   scale=3, padding=2):
    """
    Create a pixel-style text surface with background and border.
    
    Returns:
        pygame.Surface with the rendered text, background, and border
    """
    try:
        font = pg.font.SysFont('consolas', font_size)
    except:
        font = pg.font.Font(None, font_size)
    
    # Render at small size
    small_surface = font.render(text, False, text_color, bg_color)
    small_rect = small_surface.get_rect()
    
    # Add padding
    total_w = small_rect.width + padding * 2
    total_h = small_rect.height + padding * 2
    
    # Create background surface
    bg_surface = pg.Surface((total_w, total_h))
    bg_surface.fill(border_color)
    
    # Draw inner background
    inner_rect = pg.Rect(padding - 1, padding - 1, 
                         small_rect.width + 1, small_rect.height + 1)
    pg.draw.rect(bg_surface, bg_color, inner_rect)
    
    # Blit text
    bg_surface.blit(small_surface, (padding, padding))
    
    # Scale up
    scaled_surface = pg.transform.scale(bg_surface,
        (total_w * scale, total_h * scale))
    
    return scaled_surface
