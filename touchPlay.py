import pygame as py 

size1 = (900)
size2 = (700)

yellow = (255, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

screen = py.display.set_mode((size1, size2))
screen.fill(yellow)
py.display.update()

game_exit = False
while not game_exit:
    for event in py.event.get():
        if event.type == py.QUIT:
            game_exit = True

        if event.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()

            py.draw.circle(
                screen, blue, pos,100, 10
            )
            
            py.display.update()
