from Grid import Grid
from Agent import Agent
from Task import Task
from TaskList import TaskList

grid1 = Grid(5,5)
grid2 = Grid(5,5)
agent1=Agent(grid1,3,3)
agent2=Agent(grid1,1,1)
item1=Task(grid2,2,2)

Grid.printGrid(grid1)
Grid.printGrid(grid2)

while True:
    n=input()

    if(n=='q'):
        break
    elif(int(n)<=Agent.new_id and int(n)>=0):
        for a in Agent.AgentList:
            if(a.id==int(n)):
                x=input()
                if(x=='q'):
                    print("Wrong Command")
                    print(a.score)
                    break
                elif(x=='u'):
                    a.move_up()
                    Grid.printGrid(grid1)
                    Grid.printGrid(grid2)
                elif(x=='d'):
                    a.move_down()
                    Grid.printGrid(grid1)
                    Grid.printGrid(grid2)
                elif(x=='l'):
                    a.move_left()
                    Grid.printGrid(grid1)
                    Grid.printGrid(grid2)
                elif(x=='r'):
                    a.move_right()
                    Grid.printGrid(grid1)
                    Grid.printGrid(grid2)
                else:
                    print("Wrong command. Try again.")

    else:
        print("Wrong command. Try again.")
