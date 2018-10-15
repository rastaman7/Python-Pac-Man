from Grid import Grid
from Agent import Agent

grid1 = Grid(4,4)
agent1=Agent(grid1,2,2)

Grid.printGrid(grid1)

while True:
    x=input()
    if(x=='q'):
        break
    elif(x=='u'):
        agent1.move_up()
        Grid.printGrid(grid1)
    elif(x=='d'):
        agent1.move_down()
        Grid.printGrid(grid1)
    elif(x=='l'):
        agent1.move_left()
        Grid.printGrid(grid1)
    elif(x=='r'):
        agent1.move_right()
        Grid.printGrid(grid1)
    else:
        print("Wrong command. Try again.")
