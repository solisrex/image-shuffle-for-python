import pygame, sys, math
from pygame.locals import *
import random

pygame.init()

length = 500
gridsize = 4
DISPLAYSURF = pygame.display.set_mode((length,length))
BLACK = (0,0,0)
pygame.display.set_caption('Image Shuffle')
grid = [[[j,i] for i in range(gridsize)] for j in range(gridsize)]

grid[-1][-1] = None

Img = pygame.image.load('nathan-dumlao-nBJHO6wmRWw-unsplash.jpg')
Img = pygame.transform.scale(Img, (length,length))

def draw_grid():
    DISPLAYSURF.fill(BLACK)
    i=0
    for line in grid:
        j=0
        for element in line:
            if element != None:
                DISPLAYSURF.blit(Img, (j*length/gridsize,i*length/gridsize), area=((element[1]*length/gridsize,element[0]*length/gridsize),(length/gridsize,length/gridsize)))
            j+=1
        i+=1

def check_top(x,y):
    if y > 0:
        if grid[y-1][x] == None:
            return True
        else:
            return False
    else:
        return False

def check_right(x,y):
    if x < gridsize-1:
        if grid[y][x+1] == None:
            return True
        else:
            return False
    else:
        return False
    
def check_down(x,y):
    if y < gridsize-1:
        if grid[y+1][x] == None:
            return True
        else:
            return False
    else:
        return False

def check_left(x,y):
    if x > 0:
        if grid[y][x-1] == None:
            return True
        else:
            return False
    else:
        return False

def get_none_index():
    j=0
    for line in grid:
        try:
           i = line.index(None)
           return (j,i)
        except:
            j+=1
def get_adjacent_squares():
    squares = []
    j, i = get_none_index()
    if j > 0:
        squares += [(j-1,i)]
    if j < gridsize-1:
        squares += [(j+1,i)]
    if i > 0:
        squares += [(j,i-1)]
    if i < gridsize-1:
        squares += [(j,i+1)]
    return squares

def shuffle(depth):
    for count in range(depth):
        squares = get_adjacent_squares()
        j, i = get_none_index()
        sj, si = random.choice(squares)
        grid[sj][si], grid[j][i] = grid[j][i], grid[sj][si]

def main():
    shuffle(200)
    draw_grid()
    while True:
        global grid
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            if event.type ==  MOUSEBUTTONUP: 
                mousex, mousey = event.pos
                gridX = (gridsize*mousex)//length
                gridY = (gridsize*mousey)//length
                if check_top(gridX,gridY) == True:
                    grid[gridY][gridX], grid[gridY-1][gridX] = grid[gridY-1][gridX], grid[gridY][gridX]
                    draw_grid()
                elif check_right(gridX,gridY) == True:
                    grid[gridY][gridX], grid[gridY][gridX+1] = grid[gridY][gridX+1], grid[gridY][gridX]
                    draw_grid()
                elif check_down(gridX,gridY) == True:
                    grid[gridY][gridX], grid[gridY+1][gridX] = grid[gridY+1][gridX], grid[gridY][gridX]
                    draw_grid()
                elif check_left(gridX,gridY) == True:
                    grid[gridY][gridX], grid[gridY][gridX-1] = grid[gridY][gridX-1], grid[gridY][gridX]
                    draw_grid()
                    
        pygame.display.update()
main()
