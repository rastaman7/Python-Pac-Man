from Grid import Grid
from Agent import Agent
from Task import Task
from TaskList import TaskList
from Score import Score
from Qlearning import Qlearning
import random

ALPHA=0.8
GAMMA=0.2
EPSILON=0.8

grid3 = Grid()
grid4 = Grid()

for j in range(201):
    for h in Agent.AgentList:
        h.removeAgent()
    for h in TaskList.TaskList:
        h.removeTask()
    testAgent=Agent(grid3,0,2)
    testTask=Task(grid4,2,0)
    Agent.agentView()

    i=0
    while i<100:
        qtimes=0
        rnd=0
        tempQListID=-1
        if testAgent.score==1:
            break
        else:
            x=Qlearning.maxDir(testAgent)

            for c in Qlearning.QList:
                if testAgent.agentview==c.agentview and testAgent.taskview==c.taskview and x==c.direction:
                    tempQListID=c.id
                else:
                    qtimes+=1
            if qtimes-1==Qlearning.new_id:
                Qlearning(testAgent.agentview, testAgent.taskview, x, 0.0)
                tempQListID=qtimes

            if j==0 or j==1 or j==2 or j==10 or j==20 or j==100:
                print(i,":",x ,Qlearning.maxQ(testAgent),Qlearning.maxDir(testAgent))

            if(x=='u'):
                testAgent.move_up()
            elif(x=='d'):
                testAgent.move_down()
            elif(x=='l'):
                testAgent.move_left()
            elif(x=='r'):
                testAgent.move_right()
            else:
                print("Wrong command. Try again.")

            Agent.agentView()
            for d in Qlearning.QList:
                if d.id==tempQListID:
                    if grid4.cells[testAgent.row][testAgent.col]==1:
                        d.qvalue=d.qvalue+ALPHA*(1.0+GAMMA*Qlearning.maxQ(testAgent)-d.qvalue)
                    else:
                        d.qvalue=d.qvalue+ALPHA*(GAMMA*Qlearning.maxQ(testAgent)-d.qvalue)


            Score.checkScore(testAgent,grid4)
            Agent.agentView()

        i+=1

path='QList2.txt'
f=open(path,'w')

for e in Qlearning.QList:
    if e.qvalue>=0.0:
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
