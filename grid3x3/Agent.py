from Grid import Grid
from TaskList import TaskList

class Agent:

    new_id = -1
    AgentList=[]
    view_row=5
    view_col=5
    view_row_mid=int((view_row-1)/2)
    view_col_mid=int((view_col-1)/2)

    @staticmethod
    def __getNewID():
        Agent.new_id += 1
        return Agent.new_id


    def agentView():
        for a in Agent.AgentList:
            a.agentview=[]
            a.taskview=[]

            for i in range(Agent.view_row):
                a.agentview.append([0 for i in range(Agent.view_col)])
                a.taskview.append([0 for i in range(Agent.view_col)])

            for i in range(Agent.view_row):
                for j in range(Agent.view_col):
                    if a.row-(Agent.view_row_mid-i)<0 or a.row-(Agent.view_row_mid-i)>Grid.row_num-1:
                        a.agentview[i][j]=-1
                        a.taskview[i][j]=-1
                    elif a.col-(Agent.view_col_mid-j)<0 or a.col-(Agent.view_col_mid-j)>Grid.col_num-1:
                        a.agentview[i][j]=-1
                        a.taskview[i][j]=-1
                    else:
                        for b in Agent.AgentList:
                            if b.row==a.row-(Agent.view_row_mid-i) and b.col==a.col-(Agent.view_col_mid-j):
                                a.agentview[i][j]=1
                        for c in TaskList.TaskList:
                            if c.row==a.row-(Agent.view_row_mid-i) and c.col==a.col-(Agent.view_col_mid-j):
                                a.taskview[i][j]=1




    def __init__(self, grid, row, col):
        self.id = Agent.__getNewID()
        self.grid=grid
        self.row=row
        self.col=col
        self.score=0
        self.agentview=[]
        self.taskview=[]

        for i in range(Agent.view_row):
            self.agentview.append([0 for i in range(Agent.view_col)])
            self.taskview.append([0 for i in range(Agent.view_col)])

        self.grid.cells[row][col]=1
        Agent.AgentList.append(self)

    def move_up(self):
        if self.row>0 and self.grid.cells[self.row-1][self.col] != 1:
            self.row=self.row-1
            self.grid.cells[self.row][self.col]=1
            self.grid.cells[self.row+1][self.col]=0
        #else:
            #print("unable to move up")

    def move_down(self):
        if self.row<self.grid.row_num-1 and self.grid.cells[self.row+1][self.col] != 1:
            self.row=self.row+1
            self.grid.cells[self.row][self.col]=1
            self.grid.cells[self.row-1][self.col]=0
        #else:
            #print("unable to move down")

    def move_left(self):
        if self.col>0 and self.grid.cells[self.row][self.col-1] != 1:
            self.col=self.col-1
            self.grid.cells[self.row][self.col]=1
            self.grid.cells[self.row][self.col+1]=0
        #else:
            #print("unable to move left")

    def move_right(self):
        if self.col<self.grid.col_num-1 and self.grid.cells[self.row][self.col+1] != 1:
            self.col=self.col+1
            self.grid.cells[self.row][self.col]=1
            self.grid.cells[self.row][self.col-1]=0
        #else:
            #print("unable to move right")

    def earn_score(self):
        self.score=self.score+1
    def get_score(self):
        return self.score

    def printAgentView(self):
        for i in range(3):
            print(self.agentview[i])
        print("-------")

    def printTaskView(self):
        for i in range(3):
            print(self.taskview[i])
        print("-------")

    def moveAgent(self, newrow, newcol):
        self.row=newrow
        self.col=newcol

    def removeAgent(self):
        self.grid.cells[self.row][self.col]=0
        Agent.AgentList.remove(self)
        del self
