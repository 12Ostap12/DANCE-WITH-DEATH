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
car = Player('mercedes.png', 295, 470, 225, 150, 10 )
car.rotate(270)
bg = image.load('road.jpg')

enemy = Enemy('nisan.png', 200, 470, 200, 120, 10)
enemy.rotate(90)
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
        enemy.draw(window)
        enemy.update()
        car.draw(window)
        car.move()

    display.update()
    clock.tick(60)