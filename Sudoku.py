import os
import pygame
import pygame.freetype
import time

algoGrid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

protValues = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
                 [5, 2, 0, 0, 0, 0, 0, 0, 0],
                 [0, 8, 7, 0, 0, 0, 0, 3, 1],
                 [0, 0, 3, 0, 1, 0, 0, 8, 0],
                 [9, 0, 0, 8, 6, 3, 0, 0, 5],
                 [0, 5, 0, 0, 9, 0, 6, 0, 0],
                 [1, 3, 0, 0, 0, 0, 2, 5, 0],
                 [0, 0, 0, 0, 0, 0, 0, 7, 4],
                 [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

tempNum = [  [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0] ]

solution = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 1, 0] ]

def setUp():
    global screen
    global run
    global selected
    selected = False
    run = True
    screen = pygame.display.set_mode((630,700))
    screen.fill((255,255,255))
    pygame.display.set_caption("Sudoku")

def drawLines():
    for i in range (1, 10):
        pygame.draw.line(screen, (0,0,0), (0, i * 70), (630, i* 70), 1)
        pygame.draw.line(screen, (0,0,0), (i * 70, 70), (i* 70, 700), 1)
    for i in range (1, 3):
        pygame.draw.line(screen, (0,0,0), (0, 70 + i * 210), (630, 70 + i* 210), 5)
        pygame.draw.line(screen, (0,0,0), (i * 210, 70), (i* 210, 700), 5)

def highlightRect(mouse_x, mouse_y):
    corner_x = int(mouse_x/70) * 70
    corner_y = int(mouse_y/70) * 70
    pygame.draw.line(screen, (255,0,0), (corner_x, corner_y), (corner_x + 70, corner_y), 5)
    pygame.draw.line(screen, (255,0,0), (corner_x, corner_y + 70), (corner_x + 70, corner_y + 70), 5)
    pygame.draw.line(screen, (255,0,0), (corner_x + 70, corner_y), (corner_x + 70, corner_y + 70), 5)
    pygame.draw.line(screen, (255,0,0), (corner_x, corner_y), (corner_x, corner_y + 70), 5)

def drawX():
    for i in range(xCount):
        pygame.draw.line(screen, (255,0,0), (0 + i*50, 0), (50 + i*50, 50), 5)
        pygame.draw.line(screen, (255,0,0), (50 + i*50, 0), (0 + i*50, 50), 5)

def drawText(g):
    for i in range(9):
        for j in range(9):
            if (algoSolver and algoGrid[i][j] != 0):
                myfont.render_to(screen, (j*70 + 20, i*70 + 90), str(g[i][j]), (0, 0, 0))
            else:
                if (grid[i][j] != 0):
                    myfont.render_to(screen, (j*70 + 20, i*70 + 90), str(grid[i][j]), (0, 0, 0))

def winScreen():
    screen.fill((255, 255, 255))
    myfont.render_to(screen, (180, 700/2 - 100), "Sudoku Solved", (0, 0, 0))

def checkSolve():
    for i in range(9):
        for j in range(9):
            if (grid[i][j] != solution[i][j]):
                return False
    return True

def keyPicking(mouse_x, mouse_y, num):
    if (protValues[int(mouse_y/70-1)][int(mouse_x/70)] == 0):
        tempNum[int(mouse_y/70-1)][int(mouse_x/70)] = num

def drawTempNums():
    for i in range(9):
        for j in range(9):
            if (tempNum[i][j] > 0):
                tinyfont.render_to(screen, (j*70 + 52, i*70 + 75), str(tempNum[i][j]), (169, 169, 169))

def devProtValues():
    for i in range(9):
        for j in range(9):
            if (protValues[i][j] > 0):
                protValues[i][j] = 1

def loseScreen():
    screen.fill((255, 255, 255))
    myfont.render_to(screen, (180, 700/2 - 100), "Sudoku Failed", (0, 0, 0))


def printGrid(g):
    for i in range(9):
        for j in range(9):
            print(g[i][j], end = " ")
        print("")

def checkIfSafe(g, row, col, number):
    for i in range(9):
        if (g[i][col] == number or g[row][i] == number):
            return False
    boxRow = int(row/3) * 3
    boxCol = int(col/3) * 3
    for i in range(3):
        for j in range(3):
            if (g[i + boxRow][j + boxCol] == number):
                return False
    return True

def findEmptyPos(g):
    for i in range(9):
        for j in range(9):
            if (g[i][j] == 0):
                return (i * 9 + j)
    return -1;

def solve(g):
    pos = findEmptyPos(g)
    if (pos == -1):
        return True
    else:
        row = int(pos/9)
        col = pos % 9
    for i in range(1, 10):
        if (checkIfSafe(g, row, col, i)):
            g[row][col] = i
            if (solve(g)):
                return True
            g[row][col] = 0
    return False

def solveAndShow(g):
    algoSolver = True
    screen.fill((255, 255, 255))
    drawLines()
    drawText(algoGrid)
    printGrid(algoGrid)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    pos = findEmptyPos(g)
    if (pos == -1):
        return True
    else:
        row = int(pos/9)
        col = pos % 9
    for i in range(1, 10):
        if (checkIfSafe(g, row, col, i)):
            g[row][col] = i
            if (solveAndShow(g)):
                return True
            g[row][col] = 0
    return False

solve(solution)
pygame.font.init()
pygame.freetype.init()
myfont = pygame.freetype.Font("TNR.ttf", 48)
tinyfont = pygame.freetype.Font("TNR.ttf", 32)
setUp()
drawLines()
devProtValues()
mouse_x = 0
mouse_y = 0
algoSolver = False
algoFinished = False
xCount = 0

while run:
    pygame.display.update()
    screen.fill((255, 255, 255))
    drawLines()
    drawText(grid)
    drawX()
    drawTempNums()
    if (selected and mouse_y > 70):
        highlightRect(mouse_x, mouse_y)
    if pygame.mouse.get_pressed()[0]:
        selected = True
        mouse_x, mouse_y = pygame.mouse.get_pos()
    if (checkSolve() or algoFinished):
        winScreen()
    if (xCount > 3):
        loseScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if (selected):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    algoSolver = True
                    solveAndShow(algoGrid)
                    algoSolver = False
                    algoFinished = True
                    winScreen()
                if event.key == pygame.K_BACKSPACE:
                    grid[int(mouse_y/70 - 1)][int(mouse_x/70)] = 0
                    tempNum[int(mouse_y/70 - 1)][int(mouse_x/70)] = 0
                if event.key == pygame.K_RETURN:
                    num = tempNum[int(mouse_y/70-1)][int(mouse_x/70)]
                    if (num != 0 and protValues[int(mouse_y/70-1)][int(mouse_x/70)] == 0):
                        grid[int(mouse_y/70 - 1)][int(mouse_x/70)] = num
                        selected = False
                        tempNum[int(mouse_y/70-1)][int(mouse_x/70)] = 0
                    if (solution[int(mouse_y/70-1)][int(mouse_x/70)] != num and protValues[int(mouse_y/70-1)][int(mouse_x/70)] == 0):
                        xCount += 1
                if event.key == pygame.K_1:
                    keyPicking(mouse_x, mouse_y, 1)
                if event.key == pygame.K_2:
                    keyPicking(mouse_x, mouse_y, 2)
                if event.key == pygame.K_3:
                    keyPicking(mouse_x, mouse_y, 3)
                if event.key == pygame.K_4:
                    keyPicking(mouse_x, mouse_y, 4)
                if event.key == pygame.K_5:
                    keyPicking(mouse_x, mouse_y, 5)
                if  event.key == pygame.K_6:
                    keyPicking(mouse_x, mouse_y, 6)
                if event.key == pygame.K_7:
                    keyPicking(mouse_x, mouse_y, 7)
                if event.key == pygame.K_8:
                    keyPicking(mouse_x, mouse_y, 8)
                if event.key == pygame.K_9:
                    keyPicking(mouse_x, mouse_y, 9)
