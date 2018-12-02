from Grid import Grid
from Agent import Agent
from Task import Task
from TaskList import TaskList
from Score import Score


grid1 = Grid()
grid2 = Grid()
Agent(grid1,2,1)
Agent(grid1,3,3)
Task(grid2,2,2)
Task(grid2,4,4)

Agent.agentView()

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
                    Score.checkScore(a,grid2)
                    Grid.printGrid(grid1)
                    Grid.printGrid(grid2)
                elif(x=='d'):
                    a.move_down()
                    Score.checkScore(a,grid2)
                    Grid.printGrid(grid1)
                    Grid.printGrid(grid2)
                elif(x=='l'):
                    a.move_left()
                    Score.checkScore(a,grid2)
                    Grid.printGrid(grid1)
                    Grid.printGrid(grid2)
                elif(x=='r'):
                    a.move_right()
                    Score.checkScore(a,grid2)
                    Grid.printGrid(grid1)
                    Grid.printGrid(grid2)
                else:
                    print("Wrong command. Try again.")
        Agent.agentView()
        print(TaskList.TaskList)
        for b in Agent.AgentList:
            print(b.score)
            b.printAgentView()
            b.printTaskView()
    else:
        print("Wrong command. Try again.")
