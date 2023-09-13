import pygame as py

# Initializing the Pygame Library
py.init()

# This the display where we can see our game
display = py.display.set_mode((1000, 750))

# Changing the name of the game
py.display.set_caption("Tic-Tac-Toe")

# Changing the icon of the game
py.display.set_icon(py.image.load("tic-tac-toe2.png"))

# Crosses and Circles co-ordinates
cross_x1, cross_y1 = 50, 175
circle_x1, circle_y1 = 850, 175
cross_x2, cross_y2 = 50, 275
circle_x2, circle_y2 = 850, 275
cross_x3, cross_y3 = 50, 375
circle_x3, circle_y3 = 850, 375
cross_x4, cross_y4 = 50, 475
circle_x4, circle_y4 = 850, 475
cross_x5, cross_y5 = 50, 575
circle_x5, circle_y5 = 850, 575


# Cross Class
class Cross:
    def __init__(self, x, y):
        display.blit(py.image.load("cross4.png"), (x, y))


# Circle Class
class Circle:
    def __init__(self, x, y):
        display.blit(py.image.load("O.png"), (x, y))


display_on, it, select_shape = True, True, ""    # Game running loop (display on and off, loop variable, shape selector)
G1, G2, G3, G4, G5, G6, G7, G8, G9 = False, False, False, False, False, False, False, False, False
while display_on:
    display.fill((214, 234, 248))
    for event in py.event.get():
        if event.type == py.QUIT:
            display_on = False

    mouse_x1, mouse_y1 = py.mouse.get_pos()
    click1 = py.mouse.get_pressed()[0]
    # print(mouse_x1, mouse_y1)
    
    if it and click1:
        print("1st if")
        if 50 <= mouse_x1 <= 115:
            print("2nd if")
            if 175 <= mouse_y1 <= 240:
                select_shape = "cross 1"
                it = False
                print("cr 1st")
            elif 275 <= mouse_y1 <= 340:
                select_shape = "cross 2"
                it = False
                print("cr 2nd")
            elif 375 <= mouse_y1 <= 440:
                select_shape = "cross 3"
                it = False
                print("cr 3rd")
            elif 475 <= mouse_y1 <= 540:
                select_shape = "cross 4"
                it = False
                print("cr 4th")
            elif 575 <= mouse_y1 <= 640:
                select_shape = "cross 5"
                it = False
                print("cr 5th")
        elif 845 <= mouse_x1 <= 915:
            print("2nd elif")
            if 175 <= mouse_y1 <= 240:
                select_shape = "circle 1"
                it = False
                print("ci 1st")
            elif 275 <= mouse_y1 <= 340:
                select_shape = "circle 2"
                it = False
                print("ci 2nd")
            elif 375 <= mouse_y1 <= 440:
                select_shape = "circle 3"
                it = False
                print("ci 3rd")
            elif 475 <= mouse_y1 <= 540:
                select_shape = "circle 4"
                it = False
                print("ci 4th")
            elif 575 <= mouse_y1 <= 640:
                select_shape = "circle 5"
                it = False
                print("ci 5th")

    else:
        print("1st else")

        click = py.mouse.get_pressed()[0]
        mouse_x, mouse_y = py.mouse.get_pos()

        if click and (250 <= mouse_x <= 390) and (150 <= mouse_y <= 295) and (not G1):
            print("3rd 1st if")
            if select_shape == "cross 1":
                cross_x1, cross_y1 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid cr 1")
            elif select_shape == "circle 1":
                circle_x1, circle_y1 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid ci 1")
            elif select_shape == "cross 2":
                cross_x2, cross_y2 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid cr 2")
            elif select_shape == "circle 2":
                circle_x2, circle_y2 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid ci 2")
            elif select_shape == "cross 3":
                cross_x3, cross_y3 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid cr 3")
            elif select_shape == "circle 3":
                circle_x3, circle_y3 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid ci 3")
            elif select_shape == "cross 4":
                cross_x4, cross_y4 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid cr 4")
            elif select_shape == "circle 4":
                circle_x4, circle_y4 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid ci 4")
            elif select_shape == "cross 5":
                cross_x5, cross_y5 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid cr 5")
            elif select_shape == "circle 5":
                circle_x5, circle_y5 = 290, 200
                select_shape = ""
                it, G1 = True, True
                print("1st grid ci 5")
        elif click and (415 <= mouse_x <= 590) and (150 <= mouse_y <= 295) and (not G2):
            print("3rd 2nd elif")
            if select_shape == "cross 1":
                cross_x1, cross_y1 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid cr 1")
            elif select_shape == "circle 1":
                circle_x1, circle_y1 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid ci 1")
            elif select_shape == "cross 2":
                cross_x2, cross_y2 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid cr 2")
            elif select_shape == "circle 2":
                circle_x2, circle_y2 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid ci 2")
            elif select_shape == "cross 3":
                cross_x3, cross_y3 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid cr 3")
            elif select_shape == "circle 3":
                circle_x3, circle_y3 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid ci 3")
            elif select_shape == "cross 4":
                cross_x4, cross_y4 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid cr 4")
            elif select_shape == "circle 4":
                circle_x4, circle_y4 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid ci 4")
            elif select_shape == "cross 5":
                cross_x5, cross_y5 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid cr 5")
            elif select_shape == "circle 5":
                circle_x5, circle_y5 = 475, 200
                select_shape = ""
                it, G2 = True, True
                print("2nd grid ci 5")
        elif click and (615 <= mouse_x <= 750) and (150 <= mouse_y <= 295) and (not G3):
            print("3rd 3rd elif")
            if select_shape == "cross 1":
                cross_x1, cross_y1 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid cr 1")
            elif select_shape == "circle 1":
                circle_x1, circle_y1 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid ci 1")
            elif select_shape == "cross 2":
                cross_x2, cross_y2 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid cr 2")
            elif select_shape == "circle 2":
                circle_x2, circle_y2 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid ci 2")
            elif select_shape == "cross 3":
                cross_x3, cross_y3 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid cr 3")
            elif select_shape == "circle 3":
                circle_x3, circle_y3 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid ci 3")
            elif select_shape == "cross 4":
                cross_x4, cross_y4 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid cr 4")
            elif select_shape == "circle 4":
                circle_x4, circle_y4 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid ci 4")
            elif select_shape == "cross 5":
                cross_x5, cross_y5 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid cr 5")
            elif select_shape == "circle 5":
                circle_x5, circle_y5 = 650, 200
                select_shape = ""
                it, G3 = True, True
                print("3rd grid ci 5")
        elif click and (250 <= mouse_x <= 390) and (317 <= mouse_y <= 495) and (not G4):
            print("3rd 4th elif")
            if select_shape == "cross 1":
                cross_x1, cross_y1 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid cr 1")
            elif select_shape == "circle 1":
                circle_x1, circle_y1 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid ci 1")
            elif select_shape == "cross 2":
                cross_x2, cross_y2 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid cr 2")
            elif select_shape == "circle 2":
                circle_x2, circle_y2 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid ci 2")
            elif select_shape == "cross 3":
                cross_x3, cross_y3 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid cr 3")
            elif select_shape == "circle 3":
                circle_x3, circle_y3 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid ci 3")
            elif select_shape == "cross 4":
                cross_x4, cross_y4 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid cr 4")
            elif select_shape == "circle 4":
                circle_x4, circle_y4 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid ci 4")
            elif select_shape == "cross 5":
                cross_x5, cross_y5 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid cr 5")
            elif select_shape == "circle 5":
                circle_x5, circle_y5 = 290, 375
                select_shape = ""
                it, G4 = True, True
                print("4th grid ci 5")
        elif click and (415 <= mouse_x <= 590) and (317 <= mouse_y <= 495) and (not G5):
            print("3rd 5th elif")
            if select_shape == "cross 1":
                cross_x1, cross_y1 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid cr 1")
            elif select_shape == "circle 1":
                circle_x1, circle_y1 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid ci 1")
            elif select_shape == "cross 2":
                cross_x2, cross_y2 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid cr 2")
            elif select_shape == "circle 2":
                circle_x2, circle_y2 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid ci 2")
            elif select_shape == "cross 3":
                cross_x3, cross_y3 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid cr 3")
            elif select_shape == "circle 3":
                circle_x3, circle_y3 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid ci 3")
            elif select_shape == "cross 4":
                cross_x4, cross_y4 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid cr 4")
            elif select_shape == "circle 4":
                circle_x4, circle_y4 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid ci 4")
            elif select_shape == "cross 5":
                cross_x5, cross_y5 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid cr 5")
            elif select_shape == "circle 5":
                circle_x5, circle_y5 = 475, 375
                select_shape = ""
                it, G5 = True, True
                print("5th grid ci 5")
        elif click and (615 <= mouse_x <= 750) and (317 <= mouse_y <= 495) and (not G6):
            print("3rd 6th elif")
            if select_shape == "cross 1":
                cross_x1, cross_y1 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid cr 1")
            elif select_shape == "circle 1":
                circle_x1, circle_y1 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid ci 1")
            elif select_shape == "cross 2":
                cross_x2, cross_y2 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid cr 2")
            elif select_shape == "circle 2":
                circle_x2, circle_y2 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid ci 2")
            elif select_shape == "cross 3":
                cross_x3, cross_y3 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid cr 3")
            elif select_shape == "circle 3":
                circle_x3, circle_y3 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid ci 3")
            elif select_shape == "cross 4":
                cross_x4, cross_y4 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid cr 4")
            elif select_shape == "circle 4":
                circle_x4, circle_y4 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid ci 4")
            elif select_shape == "cross 5":
                cross_x5, cross_y5 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid cr 5")
            elif select_shape == "circle 5":
                circle_x5, circle_y5 = 650, 375
                select_shape = ""
                it, G6 = True, True
                print("6th grid ci 5")
        elif click and (250 <= mouse_x <= 390) and (519 <= mouse_y <= 660) and (not G7):
            print("3rd 7th elif")
            if select_shape == "cross 1":
                cross_x1, cross_y1 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid cr 1")
            elif select_shape == "circle 1":
                circle_x1, circle_y1 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid ci 1")
            elif select_shape == "cross 2":
                cross_x2, cross_y2 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid cr 2")
            elif select_shape == "circle 2":
                circle_x2, circle_y2 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid ci 2")
            elif select_shape == "cross 3":
                cross_x3, cross_y3 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid cr 3")
            elif select_shape == "circle 3":
                circle_x3, circle_y3 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid ci 3")
            elif select_shape == "cross 4":
                cross_x4, cross_y4 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid cr 4")
            elif select_shape == "circle 4":
                circle_x4, circle_y4 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid ci 4")
            elif select_shape == "cross 5":
                cross_x5, cross_y5 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid cr 5")
            elif select_shape == "circle 5":
                circle_x5, circle_y5 = 290, 555
                select_shape = ""
                it, G7 = True, True
                print("7th grid ci 5")
        elif click and (415 <= mouse_x <= 590) and (519 <= mouse_y <= 660) and (not G8):
            print("3rd 8th elif")
            if select_shape == "cross 1":
                cross_x1, cross_y1 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid cr 1")
            elif select_shape == "circle 1":
                circle_x1, circle_y1 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid ci 1")
            elif select_shape == "cross 2":
                cross_x2, cross_y2 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid cr 2")
            elif select_shape == "circle 2":
                circle_x2, circle_y2 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid ci 2")
            elif select_shape == "cross 3":
                cross_x3, cross_y3 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid cr 3")
            elif select_shape == "circle 3":
                circle_x3, circle_y3 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid ci 3")
            elif select_shape == "cross 4":
                cross_x4, cross_y4 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid cr 4")
            elif select_shape == "circle 4":
                circle_x4, circle_y4 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid ci 4")
            elif select_shape == "cross 5":
                cross_x5, cross_y5 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid cr 5")
            elif select_shape == "circle 5":
                circle_x5, circle_y5 = 475, 555
                select_shape = ""
                it, G8 = True, True
                print("8th grid ci 5")
        elif click and (615 <= mouse_x <= 750) and (519 <= mouse_y <= 660) and (not G9):
            print("3rd 9th elif")
            if select_shape == "cross 1":
                cross_x1, cross_y1 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid cr 1")
            elif select_shape == "circle 1":
                circle_x1, circle_y1 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid ci 1")
            elif select_shape == "cross 2":
                cross_x2, cross_y2 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid cr 2")
            elif select_shape == "circle 2":
                circle_x2, circle_y2 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid ci 2")
            elif select_shape == "cross 3":
                cross_x3, cross_y3 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid cr 3")
            elif select_shape == "circle 3":
                circle_x3, circle_y3 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid ci 3")
            elif select_shape == "cross 4":
                cross_x4, cross_y4 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid cr 4")
            elif select_shape == "circle 4":
                circle_x4, circle_y4 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid ci 4")
            elif select_shape == "cross 5":
                cross_x5, cross_y5 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid cr 5")
            elif select_shape == "circle 5":
                circle_x5, circle_y5 = 650, 555
                select_shape = ""
                it, G9 = True, True
                print("9th grid ci 5")


# These are our 5 crosses and 5 circles
    cross1 = Cross(cross_x1, cross_y1)
    circle1 = Circle(circle_x1, circle_y1)
    cross2 = Cross(cross_x2, cross_y2)
    circle2 = Circle(circle_x2, circle_y2)
    cross3 = Cross(cross_x3, cross_y3)
    circle3 = Circle(circle_x3, circle_y3)
    cross4 = Cross(cross_x4, cross_y4)
    circle4 = Circle(circle_x4, circle_y4)
    cross5 = Cross(cross_x5, cross_y5)
    circle5 = Circle(circle_x5, circle_y5)


# These are the four lines of the tic-tac-toe game
    display.blit(py.image.load("minus2.png"), (250, 50))
    display.blit(py.image.load("minus2.png"), (250, 250))
    display.blit(py.image.load("minus21.png"), (150, 150))
    display.blit(py.image.load("minus21.png"), (350, 150))

# These are the two players
    display.blit(py.image.load("player 1.png"), (50, 65))
    display.blit(py.image.load("player 2.png"), (850, 65))

# This simply updates the display everytime the while loop runs.
# updates the elements and events on the surface or display.
    py.display.update()
