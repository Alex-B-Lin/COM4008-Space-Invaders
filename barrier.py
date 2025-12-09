import pygame

class BarrierBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 6))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update_color(self):
        if self.hp == self.max_hp:
            color = (0, 255, 0)
        elif self.hp == 2:
            color = (170, 255, 0)
        elif self.hp == 1:
            color = (255, 200, 0)
        else:
            color = (0, 0, 0, 0)
        self.image.fill(color)

    def damage(self, amount=1):
        self.hp -= amount
        if self.hp <= 0:
            self.kill()
        else:
            self.update_color()
def create_barrier(
    x_start, y_start, width_blocks=12, height_blocks=6, gap=0):
    blocks = pygame.sprite.Group()
    for row in range(height_blocks):
        for col in range(width_blocks):
            bx = x_start + col * (6 + gap)
            by = y_start + row * (6 + gap)
            blocks.add(BarrierBlock(bx, by))
    return blocks
    # Pattern for a single barrier.
# 'X' = place a block, ' ' = empty space.
BARRIER_PATTERN = [
    "   XXXX   ",
    "  XXXXXX  ",
    " XXXXXXXX ",
    " XXXXXXXX ",
    " XXX  XXX ",
    " XX    XX ",
]

def create_barrier_from_pattern(x_start, y_start, pattern=BARRIER_PATTERN, gap=0):
    blocks = pygame.sprite.Group()
    block_size = 6  # must match BarrierBlock size (6x6)

    for row_index, row in enumerate(pattern):
        for col_index, ch in enumerate(row):
            if ch == "X":
                bx = x_start + col_index * (block_size + gap)
                by = y_start + row_index * (block_size + gap)
                block = BarrierBlock(bx, by, max_hp=3)
                blocks.add(block)

    return blocks
