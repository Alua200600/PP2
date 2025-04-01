import pygame, random
pygame.init()
WIDTH, HEIGHT = 400, 600
SPEED = 3  
FPS = 60
WHITE, RED = (255, 255, 255), (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg = pygame.image.load("C:\\Users\\alua\\Desktop\\PP2\\lab9\\images\\AnimatedStreet.png")
player_img = pygame.image.load("C:\\Users\\alua\\Desktop\\PP2\\lab9\\images\\Player.png")
enemy_img = pygame.image.load("C:\\Users\\alua\\Desktop\\PP2\\lab9\\images\\Enemy.png")
coin_img = pygame.image.load("C:\\Users\\alua\\Desktop\\PP2\\lab9\\images\\coin.png")

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
    def __init__(self):
        super().__init__(coin_img, 0, 0)
        self.randomize()

    def randomize(self):
        #Randomizes coin position and size
        size_options = {30: 1, 50: 2, 70: 3}   # Different sizes and point values
        self.size = random.choice(list(size_options.keys()))
        self.points = size_options[self.size]
        self.image = pygame.transform.scale(coin_img, (self.size, self.size))
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 40)))

    def update(self, player, score):
        #Checks for collision with the player and updates score
        if self.rect.colliderect(player.rect):
            score["coins"] += self.points
            self.randomize()

# Create game objects
player = Player(player_img, WIDTH // 2, HEIGHT - 80)
enemy = Enemy(enemy_img, random.randint(40, WIDTH - 40), -50)
coin = Coin()
all_sprites = pygame.sprite.Group(player, enemy, coin)
score = {"coins": 0}
last_speed_increase = 0

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
    # Increase enemy speed every 5 collected coins
    if score['coins'] // 5 > last_speed_increase:
        SPEED += 1
        last_speed_increase = score['coins'] // 5
    
    # Check for collision with enemy
    if player.rect.colliderect(enemy.rect):
        draw_text("Game Over", WIDTH // 3, HEIGHT // 2, RED)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
