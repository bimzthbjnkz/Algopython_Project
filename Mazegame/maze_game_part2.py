

from pygame import *

# Inisialisasi pygame
init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)  # Bisa juga pakai super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y) 
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if (self.rect.x <= win_width - 80 and self.x_speed > 0) or (self.rect.x >= 0 and self.x_speed < 0):
            self.rect.x += self.x_speed
    
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        if (self.rect.y <= win_height - 80 and self.y_speed > 0) or (self.rect.y >= 0 and self.y_speed < 0):
            self.rect.y += self.y_speed

        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        
    def fire(self):
        bullet = Bullet('', self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)


# the enemy sprite class   
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Calling the class constructor (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    #movement of an enemy
    def update(self):
        if self.rect.x <= 540: #w1.wall_x + w1.wall_width
            self.side = "right"
        if self.rect.x >= win_width-85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

# the bullet sprite's class  
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Calling the class constructor (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    #movement of an enemy
    def update(self):
        self.rect.x += self.speed
        # disappears after reaching the edge of the screen
        if self.rect.x > win_width+10:
            self.kill()        

# Membuat window
win_width = 800
win_height = 600
display.set_caption("Maze")
window = display.set_mode((win_width, win_height))
background_color = (0, 60, 140)

barriers = sprite.Group()
bullets = sprite.Group()

# Membuat tembok
walls = [
    (370, 80, 300, 50), (370, 0, 50, 250), (85, 0, 50, 200),
    (85, 350, 50, 400), (240, 350, 300, 50), (230, 100, 50, 400),
    (370, 480, 280, 50), (630, 250, 50, 500), (510, 220, 170, 50)
]
for wall in walls:
    barriers.add(GameSprite('C:/Program Files/Algoritmika/vscode/data/extensions/algoritmika.algopython-20250402.152508.0/temp/Walls.png', *wall))

# Pemain
plyr = Player('C:/Program Files/Algoritmika/vscode/data/extensions/algoritmika.algopython-20250402.152508.0/temp/Player_Sprite.png', 5, win_height - 80, 70, 70, 0, 0)

# Target akhir
final_sprite = GameSprite('C:/Program Files/Algoritmika/vscode/data/extensions/algoritmika.algopython-20250402.152508.0/temp/Done.png', win_width - 85, win_height - 100, 80, 100)

finish = False
run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                plyr.x_speed = -10
            elif e.key == K_RIGHT:
                plyr.x_speed = 10
            elif e.key == K_UP:
                plyr.y_speed = -10
            elif e.key == K_DOWN:
                plyr.y_speed = 10
            elif e.key == K_SPACE:
                plyr.fire()

        elif e.type == KEYUP:
            if e.key in (K_LEFT, K_RIGHT):
                plyr.x_speed = 0
            if e.key in (K_UP, K_DOWN):
                plyr.y_speed = 0

    if not finish:
        window.fill(background_color)
        barriers.draw(window)
        final_sprite.reset()
        plyr.reset()
        plyr.update()

        # Jika kalah (kena tembok)
    if sprite.spritecollide(plyr, barriers, False):
        finish = False
       

    if sprite.collide_rect(plyr, final_sprite):
        finish = True
        img = image.load('jumpscare.png')
        lose = transform.scale(img, (win_width,win_height ))
        window.blit(lose, (0, 0))
        display.update()
        time.delay(3000)  # Tampilkan jumpscare selama 2 detik
        run = False  # Hentikan game setelah menang

    display.update()
