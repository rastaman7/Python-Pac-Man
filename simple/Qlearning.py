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

    def maxQ(agentview, taskview):
        maxvalue=0
        for a in Qlearning.QList:
            if a.agentview==agentview and a.taskview==taskview and a.qvalue>maxvalue:
                maxvalue=a.qvalue
        return maxvalue
