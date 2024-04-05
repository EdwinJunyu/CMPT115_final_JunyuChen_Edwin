import turtle
import random
import time
import math
                      
def initializeTheCells():
    for i in range(35):
        cells.append([])
        for j in range(35):
            newCell = turtle.Turtle()
            newCell.penup()
            newCell.shape("square")
            newCell.shapesize(stretch_wid = 0.9, stretch_len = 0.9)
            cells[i].append(newCell)
            newCell.state = 0
            newCell.color("gray90") #gray90 almost white


def selectCells(x, y):
    if onClick:
        if x > -350 and x < 350 and y > -350 and y < 350:
            j = math.floor((x + 350)/20)
            i = math.floor((350 - y)/20)
            if cells[i][j].state == 0:
                cells[i][j].state = 1
                cells[i][j].color("gray0") #black
            else:
                cells[i][j].state = 0
                cells[i][j].color("gray90") #gray90 almost white
    wn.update()

def showTheUniverse():
    ycor = 340
    for i in range(35):
        xcor = -340
        for j in range(35):
            cells[i][j].goto(xcor, ycor)
            xcor += 20
        ycor -= 20
    wn.update()

def getNeighbors(i, j):
    ###### YOUR CODE #####
    # For a cell at row i and column j returns the sum of the neighbors' cell
    # values by considering the boundary condition
    # Remove the "pass" keyword at the end
    neighbors_state = []
    live_neighbors_count = 0
    offsets = [(-1, -1), (-1, 0), (-1, 1),  #The Surrounding Area of the Cell
               (0, -1), (0, 1),
               (1, -1), (1, 0), (1, 1)]
    for offset in offsets:
        ni = i + offset[0]
        nj = j + offset[1]

        if boundaryCondition == 1:
            if 0 <= ni < 35 and 0 <= nj < 35:   # 35 * 35
                neighbors_state.append(cells[ni][nj].state)
        elif boundaryCondition == 2:
            ni = ni % 35
            nj = nj % 35
            neighbors_state.append(cells[ni][nj].state)

    live_neighbors_count = sum(neighbors_state)

    return live_neighbors_count

color_palette = ["gray90", "gray80", "gray70", "gray60", "gray50"] # extra part
def updateCells():
    ###### YOUR CODE #####
    #Update each cell to alive/dead based on the rules. Call your function getNeighbors
    # Remove the "pass" keyword at the end

    global cells
    new_cells = [[None] * 35 for i in range(35)]

    for i in range(35):
        for j in range(35):   #state 1 is alive, state 2 is dead
            live_neighbors = getNeighbors(i, j)
            if cells[i][j].state == 1:
                if live_neighbors < 2 or live_neighbors > 3:  #If a state of a cell is 1 and has fewer than two neighbors that have states 1, it changes to 0.
                    new_cells[i][j] = 0
                else:   #If a state of a cell is 1 and has either two or three neighbors that have states 1, it remains 1.
                    new_cells[i][j] = 1
            else:   # If a state of a cell is 1 and has more than three neighbors that have states 1, it changes to 0.
                if live_neighbors == 3:
                    new_cells[i][j] = 1
                else:    #If a state of a cell is 0 and has exactly three neighbors that have states 1, it changes to 1.
                    new_cells[i][j] = 0

    for i in range(35):
        for j in range(35):
            if cells[i][j].state > 0:
                cells[i][j].state += 1
                cells[i][j].color(
                    color_palette[min(cells[i][j].state - 1, len(color_palette) - 1)])  # change the states
            else:
                cells[i][j].color("gray90")

    wn.update()

def esc():
    global stop
    stop = True

def start():
    global boundaryCondition
    global onClick

    onClick = False
    pen.clear()
    pen.write("Choose the boundary condition in the shell", font=("Verdana", 20, "normal"), align = "center")
    wn.update()
    boundaryCondition = int(input("Boundary Condition? Enter 1 for Constant or 2 for Periodic: "))
    pen.clear()
    pen.write("Press ESC to exit", font=("Verdana", 20, "normal"), align = "center")
    
    while not stop:
        wn.update()
        updateCells()
        time.sleep(0.05)
        
    pen.clear()
    pen.write("Done", font=("Verdana", 20, "normal"), align = "center")
    turtle.done()


 
wn = turtle.Screen()
wn.setup(width = 35*20 + 100, height = 35*20 + 100)
wn.tracer(0)

wn.listen()
wn.onkeypress(esc, "Escape") #Press ESC to exit
wn.onkeypress(start, "Return") #Press Enter to start
wn.onscreenclick(selectCells)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 365)
pen.write("Select the cells and then Press Enter to start", font=("Verdana", 20, "normal"), align = "center")

boundaryCondition = None
stop = False
onClick = True
cells = []

initializeTheCells() #Already done for you
showTheUniverse() #Already done for you

turtle.mainloop()
