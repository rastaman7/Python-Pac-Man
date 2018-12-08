from Grid import Grid
from Agent import Agent
from Task import Task
from TaskList import TaskList
from Score import Score
from Qlearning import Qlearning
import random

grid1 = Grid()
grid2 = Grid()
Agent(grid1,2,1)
Agent(grid1,3,3)
Task(grid2,2,2)
Task(grid2,4,4)

Agent.agentView()

Grid.printGrid(grid1)
Grid.printGrid(grid2)
ALPHA=0.8
GAMMA=0.1

count=0
while count<5000:
    qtimes=0
    tempQListID=-1
    n=random.randint(0,Agent.new_id)
    #print(n)

    if(n=='q'):
        break
    elif(int(n)<=Agent.new_id and int(n)>=0):
        for a in Agent.AgentList:
            if(a.id==int(n)):
                if(a.row==0):
                    x=random.choice('drl')
                elif(a.row==Grid.row_num-1):
                    x=random.choice('url')
                elif(a.col==0):
                    x=random.choice('udr')
                elif(a.col==Grid.col_num-1):
                    x=random.choice('udl')
                else:
                    x=random.choice('udlr')
                #print(x)
                #print(Qlearning.QList)
                #if count==0:
                    #Qlearning(a.agentview, a.taskview, x, 0.0)
                for c in Qlearning.QList:
                    if a.agentview==c.agentview and a.taskview==c.taskview and x==c.direction:
                        tempQListID=c.id
                    else:
                        qtimes+=1
                if qtimes-1==Qlearning.new_id:
                    Qlearning(a.agentview, a.taskview, x, 0.0)

                if(x=='u'):
                    a.move_up()
                elif(x=='d'):
                    a.move_down()
                elif(x=='l'):
                    a.move_left()
                elif(x=='r'):
                    a.move_right()
                else:
                    print("Wrong command. Try again.")

                if tempQListID!=-1:
                    #print("!!!!!!!!!!!!!!!!")
                    for d in Qlearning.QList:
                        if d.id==tempQListID:
                            if grid2.cells[a.row][a.col]==1:
                                d.qvalue=d.qvalue+ALPHA*(1.0+GAMMA*Qlearning.maxQ(a.agentview,a.taskview)-d.qvalue)
                                #print(Qlearning.maxQ(a.agentview,a.taskview))
                            else:
                                d.qvalue=d.qvalue+ALPHA*(GAMMA*Qlearning.maxQ(a.agentview,a.taskview)-d.qvalue)

                Score.checkScore(a,grid2)
                #Grid.printGrid(grid1)
                #Grid.printGrid(grid2)
        Agent.agentView()
        #print(TaskList.TaskList)
        #for b in Agent.AgentList:
            #print(b.score)
            #b.printAgentView()
            #b.printTaskView()
    else:
        print("Wrong command. Try again.")

    count += 1

path='QList.txt'
f=open(path,'w')

lcnt=0
for e in Qlearning.QList:
    if e.qvalue>0.7:
        f.write(str(e.id))
        f.write("\n")
        f.write(str(e.agentview))
        f.write("\n")
        f.write(str(e.taskview))
        f.write("\n")
        f.write(e.direction)
        f.write("\n")
        f.write(str(e.qvalue))
        f.write("\n")
        f.write("----------------\n")
f.close()

for f in Agent.AgentList:
    print(f.score)
