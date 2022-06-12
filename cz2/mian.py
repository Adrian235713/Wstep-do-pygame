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

# -------------------------------------------------------------------------
# Fukcje z lecji 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# cz_2
def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

# cz_2
def calculate_player_movement(keys):
    speed = 10
    delta_x = 0
    delta_y = 0
    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_d]:
        delta_x += speed
    if keys[pygame.K_a]:
        delta_x -= speed
    
    return [delta_x, delta_y]

# cz_3
def limit_position(position):
    x, y = position
    x = max(0, min(x, SCREEN_WIDTH))
    y = max(0, min(y, SCREEN_HEIGHT))
    return [x, y]

# =========================================================================
# cz_1
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('player.png', player_pos)

# cz_2
background_color = [9, 42, 121]

game_status = True
# =========================================================================
while game_status:

    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            game_status = False

# -------------------------------------------------------------------------
    # cz_2
    pressed_keys = pygame.key.get_pressed()
    delta_x, delta_y = calculate_player_movement(pressed_keys)

    player_pos[0] += delta_x
    player_pos[1] += delta_y

    player_pos = limit_position(player_pos)

    player = set_position_image(player, player_pos)


    screen_surface.fill(background_color)
# -------------------------------------------------------------------------
    print_image(player)

    pygame.display.update()
    clock.tick(60)

print("Zamykanie aplikacji")
pygame.quit()
quit()