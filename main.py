from pygame import*
from buttom import Button
from sprite import Player

window = display.set_mode((500,700))
clock = time.Clock()

game = True
pause = True

btn1 = Button(50, 50, 400, 400, 'start.png')
btn2 = Button(100, 400, 300, 120, 'exit.png')
bg = image.load('road.jpg')

bg = transform.rotate(bg,90)  
bg = transform.scale(bg, (500, 700))


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
        window.blit(bg, (0, 0)) 
    display.update()
    clock.tick(60)