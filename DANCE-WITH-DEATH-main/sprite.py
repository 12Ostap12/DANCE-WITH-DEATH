from pygame import*
from random import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
       
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def rotate(self,angle):
        self.image = transform.rotate(self.image, angle)

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 590:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 540:
            self.rect.x += self.speed

    def collide(self,enemys):
       
        for enemy in enemys:
            if enemy.rect.colliderect(self.rect):
                return True


class Enemy(GameSprite):
    def update(self):
        self.rect.y += 5
        if self.rect.y >= 700:
            self.rect.y = randint(-800,-100)
            self.rect.x = randint(0,500)
    
    def kill_collides(self,enemy):
        if self.rect.colliderect(enemy.rect):
            self.rect.x = randint(0,500)
            self.rect.y = randint(-600,-100)

    def set_cor(self,x,y):
        self.rect.x = x
        self.rect.y = y
