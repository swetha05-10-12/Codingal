import pygame
import random

pygame.init()

SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2

#bg colours
BLUE = pygame.Color('blue')
LightBlue = pygame.Color('lightblue')
DarkBlue = pygame.Color('darkblue')

#sprite colours
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


class Sprite(pygame.sprite.Sprite):

  def __init__(self, colour, width, height):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(colour)
    self.rect = self.image.get_rect()
    self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]


def update(self):
  self.rect.move_ip(self.velocity)
  boundary_hit = False
  if self.rect.left < 0 or self.rect.right > 500:
    self.velocity[0] = -self.velocity[0]
    boundary_hit = True
  if self.rect.top < 1 or self.rect.bottom > 400:
    self.velocity[1] = -self.velocity[1]
    boundary_hit = True
  if boundary_hit:
    pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
    pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENT))


def change_colour(self):
  self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))


def change_background_colour():
  global bg_colour
  bg_colour = random.choice([BLUE, LightBlue, DarkBlue])


all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Boundary Sprite')
bg_colour = BLUE
screen.fill(bg_colour)

exit = False
clock = pygame.time.Clock

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit = True
    elif event.type == SPRITE_COLOUR_CHANGE_EVENT:
      sp1.change_colour()
    elif event.type == BACKGROUND_COLOUR_CHANGE_EVENT:
      change_background_colour()

  all_sprites_list.update()
  screen.fill(bg_colour)
  all_sprites_list.draw(screen)

  pygame.display.flip()
  clock.tick(240)

pygame.quit()
