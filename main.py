from pygame import*
from button import Button
from sprite import Player, Enemy

window = display.set_mode((600,700))
clock = time.Clock()

game = True
pause = True
run = False

btn1 = Button(50, -50, 500, 500, 'start.png')
btn2 = Button(130, 400, 350, 150, 'exit.png')
car = Player('mercedes.png', 295, 470, 130, 70, 10 )
car.rotate(270)
bg = image.load('road.jpg')

enemyGroup = sprite.Group()
enemy = Enemy('nisan.png', 100, 800, 130, 75, 10)
enemy.rotate(90)
enemy1 = Enemy('citroen.png', 200, 800, 130, 75, 10)
enemy1.rotate(90)
enemy2 = Enemy('formula.png', 400, 800, 70, 130, 10)
enemy3 = Enemy('jaguar.png', 300, 800, 130, 60, 10)
enemy3.rotate(90)
enemyGroup.add(enemy)
enemyGroup.add(enemy1)
enemyGroup.add(enemy2)
enemyGroup.add(enemy3)


bg = transform.rotate(bg,90)  
bg = transform.scale(bg, (600, 700))
bg_width = bg.get_height()
tiles = 3
scroll = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:

            if e.key == K_ESCAPE:
                pause = True

    if pause == True:
        window.fill((255, 255, 255))
        if btn1.draw(window):
            pause = False
        if btn2.draw(window):
            game = False          
    else:
   
        window.blit(bg, (0,0 + scroll))
        window.blit(bg, (0,-700 + scroll))

        scroll += 3

        if scroll > 700:
            scroll = 0

        enemyGroup.draw(window)
        enemyGroup.update()

        enemy.kill_collides(enemy1)
        enemy.kill_collides(enemy2)
        enemy.kill_collides(enemy3)

        enemy1.kill_collides(enemy)
        enemy1.kill_collides(enemy2)
        enemy1.kill_collides(enemy3)     

        enemy2.kill_collides(enemy1)
        enemy2.kill_collides(enemy3)
        enemy2.kill_collides(enemy)
       
        enemy3.kill_collides(enemy1)
        enemy3.kill_collides(enemy2)
        enemy3.kill_collides(enemy)

        if car.collide([enemy1, enemy2, enemy3, enemy]):
            pause = True

            enemy.set_cor(200,200)
            enemy1.set_cor(200,200)
            enemy2.set_cor(200,200)
            enemy3.set_cor(200,200)
            
            

        car.draw(window)
        car.move()

    display.update()
    clock.tick(60)