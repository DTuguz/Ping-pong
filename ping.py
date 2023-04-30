from pygame import *

font.init()
font = font.SysFont('Arial', 36)

clock = time.Clock()
FPS = 60

speed = 10
window = display.set_mode((700, 500))
display.set_caption("Пинг-Понг")
window.fill((50,250,250))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, x=40, y=40):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x, y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.side = None
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed


player1 = Player("plat.png", 10,250,5,10,100)
player2 = Player("plat2.png", 680,250,5,10,100)
ball = GameSprite("ball-t.png", 350,250,5)

text_lose = font.render("Игрок слева победил!", True, (0, 0, 0))
text_win = font.render("Игрок справа победил!", True, (0, 0, 0))

x_speed = 5
y_speed = 5
game = True
while game:
    window.fill((50,250,250))
    for e in event.get():
       if e.type == QUIT:
           game = False

    player1.update_R()
    player1.reset()
    player2.update_L()
    player2.reset()
    ball.reset()
    ball.rect.x += x_speed
    ball.rect.y += y_speed

    if ball.rect.y > 450 or ball.rect.y < 0:
        y_speed *= -1

    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        x_speed *= -1

    if ball.rect.x < 0:
        window.blit(text_win, (200, 200))
        for e in event.get():
            if e.type == KEYDOWN:
                game = False
    
    if ball.rect.x > 700:
        window.blit(text_lose, (200, 200))
        for e in event.get():
            if e.type == KEYDOWN:
                game = False

    clock.tick(FPS)
    display.update()