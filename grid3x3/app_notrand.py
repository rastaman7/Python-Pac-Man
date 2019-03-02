from Grid import Grid
from Agent import Agent
from Task import Task
from TaskList import TaskList
from Score import Score
from Qlearning import Qlearning
import random

grid1 = Grid()
grid2 = Grid()
for i in range(10):
    agent1=Agent(grid1,0,2)
    task1=Task(grid2,2,0)

    Agent.agentView()

    #Grid.printGrid(grid1)
    #Grid.printGrid(grid2)
    ALPHA=0.8
    GAMMA=0.2

    count=0
    while count<500:
        qtimes=0
        tempQListID=-1
        n=random.randint(0,Agent.new_id)
        #print(n)

        if(n=='q'):
            break
        elif(int(n)<=Agent.new_id and int(n)>=0):
            for a in Agent.AgentList:
                if(a.id==int(n)):
                    x=Qlearning.maxDir(a)

                    for c in Qlearning.QList:
                        if a.agentview==c.agentview and a.taskview==c.taskview and x==c.direction:
                            tempQListID=c.id
                        else:
                            qtimes+=1
                    if qtimes-1==Qlearning.new_id:
                        Qlearning(a.agentview, a.taskview, x, 0.0)
                        tempQListID=qtimes

                    #if count>4500:
                        #print(a.agentview)
                        #print(a.taskview)
                        #print(x, Qlearning.maxQ(a))

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

                    Agent.agentView()
                    for d in Qlearning.QList:
                        counter=0
                        if d.id==tempQListID:
                            if grid2.cells[a.row][a.col]==1:
                                d.qvalue=d.qvalue+ALPHA*(1.0+GAMMA*Qlearning.maxQ(a)-d.qvalue)
                                #print("SCORE!!")
                            else:
                                d.qvalue=d.qvalue+ALPHA*(GAMMA*Qlearning.maxQ(a)-d.qvalue)
                                if d.qvalue<0.000000000001:
                                    d.qvalue=0
                                #print("NO SCORE")

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

    path='QList2.txt'
    f=open(path,'w')

    lcnt=0
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

    for f in Agent.AgentList:
        print(f.score)

    for h in Agent.AgentList:
        h.removeAgent()
    Agent.new_id = -1
    for h in TaskList.TaskList:
        h.removeTask()
    Task.new_id = -1
    Qlearning.QList.clear()
    Qlearning.new_id = -1
