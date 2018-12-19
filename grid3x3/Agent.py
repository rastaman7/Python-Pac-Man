from Grid import Grid
from TaskList import TaskList

class Agent:

    new_id = -1
    AgentList=[]
    view_row=5
    view_col=5

    @staticmethod
    def __getNewID():
        Agent.new_id += 1
        return Agent.new_id

    def agentView():
        for a in Agent.AgentList:
            a.agentview=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            a.taskview=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            if a.row==0:
                a.agentview[0]=[-1,-1,-1,-1,-1]
                a.agentview[1]=[-1,-1,-1,-1,-1]
                a.taskview[0]=[-1,-1,-1,-1,-1]
                a.taskview[1]=[-1,-1,-1,-1,-1]
            if a.row==1:
                a.agentview[0]=[-1,-1,-1,-1,-1]
                a.agentview[Agent.view_row-1]=[-1,-1,-1,-1,-1]
                a.taskview[0]=[-1,-1,-1,-1,-1]
                a.taskview[Agent.view_row-1]=[-1,-1,-1,-1,-1]
            if a.row==Grid.row_num-1:
                a.agentview[Agent.view_row-2]=[-1,-1,-1,-1,-1]
                a.agentview[Agent.view_row-1]=[-1,-1,-1,-1,-1]
                a.taskview[Agent.view_row-2]=[-1,-1,-1,-1,-1]
                a.taskview[Agent.view_row-1]=[-1,-1,-1,-1,-1]
            if a.col==0:
                a.agentview[0][0]=-1
                a.agentview[1][0]=-1
                a.agentview[2][0]=-1
                a.agentview[3][0]=-1
                a.agentview[4][0]=-1
                a.taskview[0][0]=-1
                a.taskview[1][0]=-1
                a.taskview[2][0]=-1
                a.taskview[3][0]=-1
                a.taskview[4][0]=-1

                a.agentview[0][1]=-1
                a.agentview[1][1]=-1
                a.agentview[2][1]=-1
                a.agentview[3][1]=-1
                a.agentview[4][1]=-1
                a.taskview[0][1]=-1
                a.taskview[1][1]=-1
                a.taskview[2][1]=-1
                a.taskview[3][1]=-1
                a.taskview[4][1]=-1
            if a.col==1:
                a.agentview[0][0]=-1
                a.agentview[1][0]=-1
                a.agentview[2][0]=-1
                a.agentview[3][0]=-1
                a.agentview[4][0]=-1
                a.taskview[0][0]=-1
                a.taskview[1][0]=-1
                a.taskview[2][0]=-1
                a.taskview[3][0]=-1
                a.taskview[4][0]=-1

                a.agentview[0][Agent.view_col-1]=-1
                a.agentview[1][Agent.view_col-1]=-1
                a.agentview[2][Agent.view_col-1]=-1
                a.agentview[3][Agent.view_col-1]=-1
                a.agentview[4][Agent.view_col-1]=-1
                a.taskview[0][Agent.view_col-1]=-1
                a.taskview[1][Agent.view_col-1]=-1
                a.taskview[2][Agent.view_col-1]=-1
                a.taskview[3][Agent.view_col-1]=-1
                a.taskview[4][Agent.view_col-1]=-1
            if a.col==Grid.col_num-1:
                a.agentview[0][Agent.view_col-1]=-1
                a.agentview[1][Agent.view_col-1]=-1
                a.agentview[2][Agent.view_col-1]=-1
                a.agentview[3][Agent.view_col-1]=-1
                a.agentview[4][Agent.view_col-1]=-1
                a.taskview[0][Agent.view_col-1]=-1
                a.taskview[1][Agent.view_col-1]=-1
                a.taskview[2][Agent.view_col-1]=-1
                a.taskview[3][Agent.view_col-1]=-1
                a.taskview[4][Agent.view_col-1]=-1

                a.agentview[0][Agent.view_col-2]=-1
                a.agentview[1][Agent.view_col-2]=-1
                a.agentview[2][Agent.view_col-2]=-1
                a.agentview[3][Agent.view_col-2]=-1
                a.agentview[4][Agent.view_col-2]=-1
                a.taskview[0][Agent.view_col-2]=-1
                a.taskview[1][Agent.view_col-2]=-1
                a.taskview[2][Agent.view_col-2]=-1
                a.taskview[3][Agent.view_col-2]=-1
                a.taskview[4][Agent.view_col-2]=-1
            for b in Agent.AgentList:
                a.agentview[b.row+2-a.row][b.col+2-a.col]=1
            for c in TaskList.TaskList:
                a.taskview[c.row-a.row+2][c.col-a.col+2]=1

    def __init__(self, grid, row, col):
        self.id = Agent.__getNewID()
        self.grid=grid
        self.row=row
        self.col=col
        self.score=0
        self.agentview=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.taskview=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

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