import pygame
pygame.init()

# =========================================================================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Pierwsza Gra')

clock = pygame.time.Clock()

# =========================================================================
# cz_1
def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()
    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

# cz_1
def print_image(img_list):
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)


# =========================================================================
# cz_1
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('player.png', player_pos)


game_status = True
# =========================================================================
while game_status:

    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            game_status = False


    print_image(player)

    pygame.display.update()
    clock.tick(60)

print("Zamykanie aplikacji")
pygame.quit()
quit()