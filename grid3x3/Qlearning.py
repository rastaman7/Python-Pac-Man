from Grid import Grid
import random
class Qlearning:

    new_id = -1
    QList=[]

    @staticmethod
    def __getNewID():
        Qlearning.new_id += 1
        return Qlearning.new_id

    def __init__(self, agentview, taskview, direction, qvalue):
        self.id = Qlearning.__getNewID()
        self.agentview=agentview
        self.taskview=taskview
        self.direction=direction
        self.qvalue=qvalue

        Qlearning.QList.append(self)

    def maxQ(agent):
        maxvalue=0
        for a in Qlearning.QList:
            if a.agentview==agent.agentview and a.taskview==agent.taskview and a.qvalue>maxvalue:
                maxvalue=a.qvalue
        return maxvalue

    def maxDir(agent):
        maxvalue2=0
        x=random.choice('udlr')

        if(agent.row==0):
            if(agent.col==0):
                x=random.choice('dr')
            elif(agent.col==Grid.col_num-1):
                x=random.choice('dl')
            else:
                x=random.choice('dlr')
        elif(agent.row==Grid.row_num-1):
            if(agent.col==0):
                x=random.choice('ur')
            elif(agent.col==Grid.col_num-1):
                x=random.choice('ul')
            else:
                x=random.choice('ulr')
        elif(agent.col==0):
            x=random.choice('udr')
        elif(agent.col==Grid.col_num-1):
            x=random.choice('udl')
        else:
            x=random.choice('udlr')

        yesrandom=x
        for a in Qlearning.QList:
            if a.agentview==agent.agentview and a.taskview==agent.taskview and a.qvalue>maxvalue2:
                #print("not random")
                x=a.direction
        #if yesrandom==x:
            #print("random")
        return x
