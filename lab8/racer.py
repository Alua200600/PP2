import pygame, random

pygame.init()
WIDTH, HEIGHT, SPEED, FPS = 400, 600, 3, 60
WHITE, RED = (255, 255, 255), (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg = pygame.image.load(r"C:\Users\alua\Desktop\PP2\lab8\images\AnimatedStreet.png")
player_img = pygame.image.load(r"C:\Users\alua\Desktop\PP2\lab8\images\Player.png")
enemy_img = pygame.image.load(r"C:\Users\alua\Desktop\PP2\lab8\images\Enemy.png")
coin_img = pygame.transform.scale(pygame.image.load(r"C:\Users\alua\Desktop\PP2\lab8\images\coin.png"), (40, 40))

font = pygame.font.SysFont("Verdana", 20)

def draw_text(text, x, y, color=WHITE):
    screen.blit(font.render(str(text), True, color), (x, y))

class Entity(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(center=(x, y))

class Player(Entity):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

class Enemy(Entity):
    def update(self):
        self.rect.y += SPEED
        if self.rect.top > HEIGHT:
            self.rect.y = -50
            self.rect.x = random.randint(40, WIDTH - 40)

class Coin(Entity):
    def update(self, player, score):
        if self.rect.colliderect(player.rect):
            score["coins"] += 1
            self.rect.y, self.rect.x = random.randint(40, HEIGHT - 40), random.randint(40, WIDTH - 40)

player = Player(player_img, WIDTH // 2, HEIGHT - 80)
enemy = Enemy(enemy_img, random.randint(40, WIDTH - 40), -50)
coin = Coin(coin_img, random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 40))
all_sprites = pygame.sprite.Group(player, enemy, coin)
score = {"coins": 0}

running = True
while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player.update()
    enemy.update()
    coin.update(player, score)
    all_sprites.draw(screen)
    draw_text(f"Coins: {score['coins']}", 10, 10)
    
    if player.rect.colliderect(enemy.rect):
        draw_text("Game Over", WIDTH // 3, HEIGHT // 2, RED)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
