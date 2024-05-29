import random, pygame, sys
from pygame.locals import *
import time
import os
import math
import mysql.connector
pygame.init()
pygame.font.init()
clock=pygame.time.Clock()

                                                                 #DATABSE AND ITS CONNECTIONS
#USE THIS TO CREATE DATABASE INITIALLY
#creating cursors
mydb = mysql.connector.connect(host="localhost",user="root",password="naqvi123",)
mycursor = mydb.cursor()
mycursor3 = mydb.cursor()
mycursor.execute("Create database GUESSTIMATION")
mycursor.execute("use GUESSTIMATION")
mycursor.execute("Create table player_info(userID varchar(29), password varchar(55))")

def databse_log_check():
    global user_login
    user=user_login
    mycursor.execute("Select userID,password from player_info")
    myresult = mycursor.fetchall()
    for row in myresult:
        if row[0] == user_login:
            return('SUCCESS')
    else:
        return('INVALID')

def PASSWORDENTRY():
    making_screen(800,500,BLACK,'GUESSTIMATION','cropped_image.png')
    clock.tick(60)
    pass_run = True
    while pass_run:
        making_screen(800, 500, BLACK, 'GUESSTIMATION', 'cropped_image.png')
        nextbut.draw(screen)
        font_object(GREY,'ENTER PASSWORD',20,70,frees,30)
        for event in pygame.event.get():
            global user_PASS
            pos = pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                pass_run=False
            if event.type == pygame.KEYDOWN:
                font = pygame.font.SysFont(frees,30)
                if event.type == pygame.K_BACKSPACE:
                    user_PASS = user_PASS[:-1]
                else:
                    user_PASS += event.unicode
                txt_surface = font.render(user_PASS, True, (255, 255, 255))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextbut.isOver(pos):
                    mycursor.execute("Select userID,password from player_info")
                    myresult = mycursor.fetchall()
                    for row in myresult:
                        print(row)
                        if row[1] == user_PASS:
                            pass_run = False
                            return ("SUCCESS")
                    else:
                        font_object(WHITE,'INVALID PASSWORD,PLEASE RE-ENTER',200,0,frees,35)
                        time.sleep(1)
                        user_login=''
                        user_PASS=''
                        PASSWORDENTRY()

def login():
    making_screen(800,500,BLACK,'GUESSTIMATION','black.png')
    clock.tick(60)
    log_run = True
    while log_run:
        making_screen(800, 500, BLACK, 'GUESSTIMATION', 'black.png')
        font_object(GREY,'ENTER USERNAME',20,70,frees,30)
        nextbut.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            global user_login
            pos = pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                log_run=False
            if event.type == pygame.KEYDOWN:
                font = pygame.font.SysFont(frees,30)
                if event.type == pygame.K_BACKSPACE:
                    user_login = user_login[:-1]
                    pygame.display.update()
                else:
                    user_login += event.unicode
                    font_object(WHITE,user_login,20,100,frees,30)
            if len(user_login)!=0 and event.type == pygame.MOUSEBUTTONDOWN:
                if nextbut.isOver(pos):
                    id_check=databse_log_check()
                    if id_check=='SUCCESS':
                        ret = PASSWORDENTRY()
                        log_run=False
                        return (ret)
                    else:
                        font_object(WHITE,'INVALID USERNAME',250,0,frees,45)
                        time.sleep(2)
                        user_login=''
                        login()
            pygame.display.flip()
            clock.tick(30)

def account_create_login():
    making_screen(800,500,BLACK,'GUESSTIMATION','black.png')
    nextbut.draw(screen)
    pygame.display.update()
    acc_create_run = True
    while acc_create_run:
        making_screen(800, 500, BLACK, 'GUESSTIMATION', 'black.png')
        font_object(GREY,'ENTER USERNAME',20,70,frees,30)
        nextbut.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            global user_login_create
            global user_create_pass
            if event.type == pygame.QUIT:
                acc_create_run = False
            else:
                if event.type == pygame.KEYDOWN:
                    font = pygame.font.SysFont(frees, 30)
                    if event.type == pygame.K_BACKSPACE:
                        user_login_create = user_login_create[:-1]
                        pygame.display.update()
                    else:
                        user_login_create += event.unicode
                    txt_surface = font.render(user_login_create, True, (255, 255, 255))
                    screen.blit(txt_surface, (20, 100))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if nextbut.isOver(pos):
                        user = user_login_create
                        mycursor.execute("Select userID from player_info")
                        myresult = mycursor.fetchall()
                        for row in myresult:
                            if row != None:
                                if row[0] == user_login_create:
                                    font_object(GREY,'USERNAME TAKEN!',250,0,frees,30)
                                    font_object(GREY,'PLEASE ENTER ANOTHER USERNAME',250,460,frees,30)
                                    time.sleep(2)
                                    pygame.display.update()
                                    acc_create_run = False
                                    user_login_create=''
                                    account_create_login()
                                    pygame.display.update()

                        else:
                            acc_create_run=False
                            RET=password_create_new(user_login_create)
                            pygame.display.update()
                            return(RET)
            clock.tick(30)
            pygame.display.flip()

def password_create_new(user_login_create):
    making_screen(800,500,BLACK,'GUESSTIMATION','cropped_image.png')
    clock.tick(60)
    pass_create_run = True
    while pass_create_run:
        making_screen(800, 500, BLACK, 'GUESSTIMATION', 'cropped_image.png')
        font = pygame.font.SysFont('freesansbold.ttf', 30)
        font_object(GREY,'ENTER PASSWORD',20,70,frees,30)
        nextbut.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            global user_PASS
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pass_create_run = False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_BACKSPACE:
                    user_PASS = user_PASS[:-1]
                    pygame.display.update()
                user_PASS += event.unicode
                font_object(WHITE, user_PASS, 20, 110, coco, 30)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextbut.isOver(pos):
                    sqlform = "INSERT INTO player_info(userID,password) VALUES(%s,%s)"
                    s=(user_login_create,user_PASS)
                    mycursor3.execute(sqlform,s)
                    mydb.commit()
                    font_object(WHITE,user_PASS,10,90,frees,30)
                    time.sleep(2)
                    pygame.display.update()
                    return ('DONE')

user_login_create = ''
user_create_pass=''
user_PASS=''
user_login=''
A = '*'

                                                                    #DISPLAY OF THE GAME
#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
CREAM=(255,253,208)
GREY=(192,192,192)

#fonts
frees='freesansbold.ttf'
coco='Courier new'

pygame.init()  # initializes the the imported pygame modules
screen = pygame.display.set_mode((800, 500))  # defines the dimensions
pygame.display.set_caption('GUESSTIMATION')  # title of the program
background = pygame.image.load('black.png')
screen.fill(BLACK)
screen.blit(background,(0,0))

def making_screen(width,height,color_of_screen,caption,image_blit,POS=0,COL=0):
    pygame.init()  # initializes the the imported pygame modules
    screen = pygame.display.set_mode((width, height))  # defines the dimensions
    pygame.display.set_caption(caption)  # title of the program
    background = pygame.image.load(image_blit)
    screen.fill(color_of_screen)
    screen.blit(background, (POS,COL))
    pygame.display.update()

def font_object(color_of_font,text,position_colom,position_row,font_type,size_of_font):
    font = pygame.font.SysFont(font_type, size_of_font)
    font_obj = font.render(text, True, color_of_font)
    screen.blit(font_obj, (position_colom,position_row))
    pygame.display.update()

#creating the buttons
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont('freesansbold.ttf', 30)
            text = font.render(self.text, 1, (225, 225, 225))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def redrawwin():
    LOGIN.draw(screen)
    ENTERGUEST.draw(screen)
    MAKEACCOUNT.draw(screen)
    pygame.display.update()
def redrawgamechoice():
    GAMEmemoryBUTTON.draw(screen)
    GAMEhangmanBUTTON.draw(screen)
    pygame.display.update()
def nextbutton():
    NEXTBUTTON.draw(screen)
    pygame.display.update()
def redrawgamecateg():
    RANDOMWORDS.draw(screen)
    ENGLISHMOVIES.draw(screen)
    HINDIMOVIES.draw(screen)
    pygame.display.update()
def reddraw_yesno_option():
    YESOPTION.draw(screen)
    NOOPTION.draw(screen)
    pygame.display.update()

#BUTTONS
LOGIN= button((0, 0, 0), 330, 160, 100, 30, 'LOGIN')
MAKEACCOUNT=button((0, 0, 0), 330, 210, 190, 30, 'CREATE ACCOUNT')
ENTERGUEST=button((0, 0, 0), 330, 260, 180, 30, 'ENTER AS GUEST')
YESOPTION=button(BLACK,260, 310, 100, 30, 'YES')
NOOPTION=button(BLACK,260, 360, 100, 30, 'NO')
nextbut=button((0, 0, 0), 700, 480, 60, 30, 'NEXT')
NEXTBUTTON=button((0, 0, 0), 700, 590, 60, 30, 'NEXT')
GAMEmemoryBUTTON=button((0, 0, 0),350, 160, 100, 30, 'MEMORY GAME')
GAMEhangmanBUTTON=button((0, 0, 0),350, 210, 100, 30, 'HANGMAN')
RANDOMWORDS=button((0, 0, 0),350, 160, 100, 30, 'RANDOM WORDS')
ENGLISHMOVIES=button((0, 0, 0),350, 210, 100, 30, 'ENGLISH MOVIES')
HINDIMOVIES=button((0, 0, 0),350, 260, 100, 30, 'HINDI MOVIES')

#DESCRIPTION OF EACH GAME
def description_hangman():
    #main setup display
    making_screen(775,470,BLACK,"HANGMAN'S ALLEY",'hangman_description.PNG')
    pygame.display.update()
    hang_run_des = True
    while hang_run_des:
        pygame.display.update()
        time.sleep(10)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                hang_run_des=False
        else:
            return('RUN CATEG')

def description_memorygame():
    making_screen(770,475, BLACK, 'MEMORY GAME', 'descrp_arya.png')
    mem_run_des=True
    while  mem_run_des:
        making_screen(770, 475, BLACK, 'MEMORY GAME', 'descrp_arya.png')
        pygame.display.update()
        time.sleep(10)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                mem_run_des=False
        return('PLAY MEMORY GAME')

def game_choicee():
    making_screen(800,500, BLACK, 'GUESSTIMATION','black.png')
    choice_run=True
    while choice_run:
        making_screen(800, 500, BLACK, 'GUESSTIMATION', 'black.png')
        font_object(WHITE,'GAMES OF GUESSTIMATION',250,100,frees,40)
        redrawgamechoice()
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                choice_run = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if GAMEmemoryBUTTON.isOver(pos):
                        choice_run=True
                        return('MEMORY GAME')
                    if GAMEhangmanBUTTON.isOver(pos):
                        choice_run=True
                        return('HANGMAN GAME')

def hangmancategory():
    making_screen(800,500, BLACK, "HANGMAN'S ALLEY",'black.png')
    pygame.display.flip()
    clock.tick(60)
    hang_categ_run=True
    while hang_categ_run:
        making_screen(800, 500, BLACK, "HANGMAN'S ALLEY", 'black.png')
        pygame.display.update()
        font_object(GREY,"PLEASE CHOOSE ANY ONE OF THE FOLLOWING CATAGORIES ",100,100,frees,30)
        main_list1=[]
        for event in pygame.event.get():
            redrawgamecateg()
            pos = pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                hang_categ_run=False
            if event.type == pygame.MOUSEBUTTONDOWN:                    #selecting the category when the mouse is over that button
                if RANDOMWORDS.isOver(pos):
                    from hangman_words import random_words              # Importing desired list from a module which contains lists of words
                    main_list1 = random_words
                    return(main_list1)

                if ENGLISHMOVIES.isOver(pos):
                    from hangman_words import eng_movies
                    main_list1 = eng_movies
                    return(main_list1)

                if HINDIMOVIES.isOver(pos):
                    from hangman_words import hindi_movies
                    main_list1 = hindi_movies
                    return(main_list1)

def hinthangman():
    making_screen(600, 552, WHITE, "HANGMAN'S ALLEY", 'GAME_CATEG.jpg', 0, 0)
    hint_run = True
    while hint_run:
        making_screen(600, 552, WHITE, "HANGMAN'S ALLEY", 'GAME_CATEG.jpg', 0, 0)
        font_object(WHITE, 'DO YOU WANT A HINT ?',150,250,coco,30)
        reddraw_yesno_option()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                hint_run = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if YESOPTION.isOver(pos):
                        hint_run=False
                        return('YES')
                    if NOOPTION.isOver(pos):
                        hint_run=False
                        return ('NO')
            clock.tick(30)
            pygame.display.flip()

def hint_screen(hint):
    making_screen(880, 502, WHITE, "HANGMAN'S ALLEY", 'hint-hacker.jpg', 0, 0)
    hint_screen_run = True
    while hint_screen_run:
        making_screen(880, 502, WHITE, "HANGMAN'S ALLEY", 'hint-hacker.jpg', 0, 0)
        if '*' in hint:
            HINT=hint.split('*')
            space_row=250
            coloumn=0
            for line in HINT:
                space_row+=30
                linee=line.lstrip()
                font_object(WHITE,linee,coloumn,space_row,coco,20)
        else:
            font_object(WHITE, hint, 0, 250, coco, 20)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                hint_screen_run = False
            pygame.display.update()
            clock.tick(30)

def solution_hang(word):
    sol_run = True
    while sol_run:
        making_screen(802, 501, CREAM, "HANGMAN'S ALLEY", 'Sorry you lost.png')
        time.sleep(1)
        pygame.display.update()
        making_screen(600, 552, CREAM, "HANGMAN'S ALLEY", 'GAME_CATEG.jpg')
        pygame.display.update()
        font_object(WHITE,'ANSWER',150,310,'freesansbold.ttf',30)
        font_object(WHITE,word,150,340,'freesansbold.ttf',30)
        time.sleep(3)
        pygame.display.update()
        sol_run=False
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sol_run = False

#MEMORY GAME-ARYA
def MEMORYGAME():
    FPS = 30
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    REVEALSPEED = 4
    BOXSIZE = 40
    GAPSIZE = 10
    BOARDWIDTH = 6
    BOARDHEIGHT = 5
    assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches'
    XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
    YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

    GRAY = (100, 100, 100)
    NAVYBLUE = (60, 60, 100)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    ORANGE = (255, 128, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    BGCOLOR = NAVYBLUE
    LIGHTBGCOLOR = GRAY
    BOXCOLOR = WHITE
    HIGHLIGHTCOLOR = BLUE
    DONUT = 'donut'
    SQUARE = 'square'
    DIAMOND = 'diamond'
    ALLCOLORS = (GREEN, BLUE, YELLOW, ORANGE, RED)
    ALLSHAPES = (DONUT, SQUARE, DIAMOND)

    assert len(ALLCOLORS) * len(
        ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

    def main():
        global FPSCLOCK, DISPLAYSURF
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        mousex = 0
        mousey = 0
        pygame.display.set_caption('Memory Game')

        mainBoard = getRandomizedBoard()
        revealedBoxes = generateRevealedBoxesData(False)

        firstSelection = None

        DISPLAYSURF.fill(BGCOLOR)

        startGameAnimation(mainBoard)

        while True:
            mouseClicked = False
            DISPLAYSURF.fill(BGCOLOR)
            drawBoard(mainBoard, revealedBoxes)

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    mouseClicked = True
            boxx, boxy = getBoxAtPixel(mousex, mousey)
            if boxx != None and boxy != None:
                if not revealedBoxes[boxx][boxy]:
                    drawHighlightBox(boxx, boxy)
                if not revealedBoxes[boxx][boxy] and mouseClicked:
                    revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                    revealedBoxes[boxx][boxy] = True

                    if firstSelection == None:
                        firstSelection = (boxx, boxy)
                    else:
                        icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                        icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)
                        if icon1shape != icon2shape or icon1color != icon2color:
                            pygame.time.wait(1000)
                            coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                            revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                            revealedBoxes[boxx][boxy] = False
                        elif hasWon(revealedBoxes):
                            gameWonAnimation(mainBoard)
                            pygame.time.wait(2000)

                            mainBoard = getRandomizedBoard()
                            revealedBoxes = generateRevealedBoxesData(False)

                            drawBoard(mainBoard, revealedBoxes)
                            pygame.display.update()
                            pygame.time.wait(1000)

                            startGameAnimation(mainBoard)
                        firstSelection = None
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def generateRevealedBoxesData(val):
        revealedBoxes = []
        for i in range(BOARDWIDTH):
            revealedBoxes.append([val] * BOARDHEIGHT)
        return revealedBoxes

    def getRandomizedBoard():
        icons = []
        for color in ALLCOLORS:
            for shape in ALLSHAPES:
                icons.append((shape, color))
        random.shuffle(icons)
        numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2)
        icons = icons[:numIconsUsed] * 2
        random.shuffle(icons)
        board = []
        for x in range(BOARDWIDTH):
            column = []
            for y in range(BOARDHEIGHT):
                column.append(icons[0])
                del icons[0]
            board.append(column)
        return board

    def splitIntoGroupsOf(groupSize, theList):
        result = []
        for i in range(0, len(theList), groupSize):
            result.append(theList[i:i + groupSize])
        return result

    def leftTopCoordsOfBox(boxx, boxy):
        left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
        top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
        return (left, top)

    def getBoxAtPixel(x, y):
        for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                left, top = leftTopCoordsOfBox(boxx, boxy)
                boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
                if boxRect.collidepoint(x, y):
                    return (boxx, boxy)
        return (None, None)

    def drawIcon(shape, color, boxx, boxy):
        quarter = int(BOXSIZE * 0.25)
        half = int(BOXSIZE * 0.5)
        left, top = leftTopCoordsOfBox(boxx, boxy)

        if shape == DONUT:
            pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
            pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
        elif shape == SQUARE:
            pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
        elif shape == DIAMOND:
            pygame.draw.polygon(DISPLAYSURF, color, (
            (left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))

    def getShapeAndColor(board, boxx, boxy):
        return board[boxx][boxy][0], board[boxx][boxy][1]

    def drawBoxCovers(board, boxes, coverage):
        for box in boxes:
            left, top = leftTopCoordsOfBox(box[0], box[1])
            pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
            shape, color = getShapeAndColor(board, box[0], box[1])
            drawIcon(shape, color, box[0], box[1])
            if coverage > 0:
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    def revealBoxesAnimation(board, boxesToReveal):
        for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, - REVEALSPEED):
            drawBoxCovers(board, boxesToReveal, coverage)

    def coverBoxesAnimation(board, boxesToCover):
        for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
            drawBoxCovers(board, boxesToCover, coverage)

    def drawBoard(board, revealed):

        for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                left, top = leftTopCoordsOfBox(boxx, boxy)
                if not revealed[boxx][boxy]:

                    pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                else:

                    shape, color = getShapeAndColor(board, boxx, boxy)
                    drawIcon(shape, color, boxx, boxy)

    def drawHighlightBox(boxx, boxy):
        left, top = leftTopCoordsOfBox(boxx, boxy)
        pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)

    def startGameAnimation(board):
        coveredBoxes = generateRevealedBoxesData(False)
        boxes = []
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                boxes.append((x, y))
        random.shuffle(boxes)
        boxGroups = splitIntoGroupsOf(8, boxes)

        drawBoard(board, coveredBoxes)
        for boxGroup in boxGroups:
            revealBoxesAnimation(board, boxGroup)
            coverBoxesAnimation(board, boxGroup)

    def gameWonAnimation(board):
        coveredBoxes = generateRevealedBoxesData(True)
        color1 = LIGHTBGCOLOR
        color2 = BGCOLOR
        for i in range(13):
            color1, color2 = color2, color1
            DISPLAYSURF.fill(color1)
            drawBoard(board, coveredBoxes)
            pygame.display.update()
            pygame.time.wait(500)

    def hasWon(revealedBoxes):
        for i in revealedBoxes:
            if False in i:
                return False
        return True

    if __name__ == '__main__':
        main()

#MAIN HANGMAN GAME-ALINA
def hangman_fullgame(main_list):
    global WHITE
    global BLACK
    # setup display
    pygame.init()  # initializes the the imported pygame modules
    WIDTH, HEIGHT = 800, 500  # setting the dimensions for the window size
    win = pygame.display.set_mode((WIDTH, HEIGHT))  # defines the dimensions
    pygame.display.set_caption("HANGMAN'S ALLEY")  # defines the title of the program
    # button variables
    RADIUS = 20
    GAP = 15
    letters = []
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 12 - 2 * RADIUS) / 2)
    starty = 400
    A = 65
    for i in range(26):
        x = startx + RADIUS + ((RADIUS * 2 + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])

    # fonts
    LETTER_FONT = pygame.font.SysFont("Book Antiqua", 25)
    WORD_FONT = pygame.font.SysFont("Book Antiqua", 40)

    # load images
    images = []
    for i in range(7):
        image = pygame.image.load("hangman" + str(i) + ".PNG")
        images.append(image)
    main_bg = pygame.image.load("main page.PNG")
    won_text = pygame.image.load("You won.PNG")

    # game variables
    display_surface = pygame.display.set_mode((800, 500 ))
    hangman_status = 0
    chances = 6
    main = random.choice(main_list)  # The word to be guessed
    word = main[0].upper()
    hint = main[1]
    guessed = []  # list for letters already guessed by user
    score = 600

    # setup game loop
    FPS = 60  # maximum frames per second
    clock = pygame.time.Clock()  # makes sure the loop runs at this speed
    run = True

    def draw():
        display_surface.blit(main_bg, (0, 0))
        win.blit(images[hangman_status], (10, 110))
        # draw buttons
        for letter in letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(win, WHITE, (x, y), RADIUS, 3)
                text = LETTER_FONT.render(ltr, 1, WHITE)
                win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

        # draw word
        display_word = ""
        for letter in word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "

        text = WORD_FONT.render(display_word, 1, WHITE)
        win.blit(text, (300, 200))

        pygame.display.update()

    while run:
        clock.tick(FPS)  # to make sure the clock runs at this speed(FPS)
        # asking for hint
        if chances == 3:
            yn = hinthangman()  # todo check name
            if yn == "YES":
                hint_screen(hint)
                hangman_status += 1
                chances -= 1
                score -= 50
                pygame.init()  # initializes the the imported pygame modules
                WIDTH, HEIGHT = 800, 500  # setting the dimensions for the window size
                win = pygame.display.set_mode((WIDTH, HEIGHT))  # defines the dimensions
                pygame.display.set_caption("HANGMAN'S ALLEY")
            else:
                pygame.init()  # initializes the the imported pygame modules
                WIDTH, HEIGHT = 800, 500  # setting the dimensions for the window size
                win = pygame.display.set_mode((WIDTH, HEIGHT))  # defines the dimensions
                pygame.display.set_caption("HANGMAN'S ALLEY")
                chances -= 1

        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # checks if user has tried to exit the game
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) **2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
                                chances -= 1

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_surface.blit(won_text, (0, 0))
            pygame.display.update()
            time.sleep(4)
            pygame.display.update()
            run=False
            pygame.display.update()

        if hangman_status > 6:
            solution_hang(word)
            pygame.display.update()

def chosen_game():
    running = False
    AA = game_choicee()
    if AA == 'MEMORY GAME':
        PLAY = description_memorygame()
        if PLAY == 'PLAY MEMORY GAME':
            MEMORYGAME()
    else:
        AAAAA = description_hangman()
        if AAAAA == 'RUN CATEG':
            main_list = hangmancategory()
            hang_categ_run = False
            hangman_fullgame(main_list)

                                                        # GAME LOOP
running = True
while running:
    making_screen(800,500,BLACK,'GUESSTIMATION','black.png')
    redrawwin()
    font_object(WHITE,"WELCOME TO GUESSTIMATION ", 175, 100, frees, 30)
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if LOGIN.isOver(pos):
                running=False
                value=login()
                if value=='SUCCESS':
                    chosen_game()
            if MAKEACCOUNT.isOver(pos):
                running=False
                value=account_create_login()
                if value=='DONE':
                    chosen_game()
            if ENTERGUEST.isOver(pos):
                chosen_game()
        clock.tick(60)
        pygame.display.update()
