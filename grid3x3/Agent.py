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
            a.agentview=[]
            a.taskview=[]

            for i in range(Agent.view_row):
                a.agentview.append([0 for i in range(Agent.view_col)])
                a.taskview.append([0 for i in range(Agent.view_col)])

            if a.row==0:
                for j in range(Agent.view_col):
                    a.agentview[0][j]=-1
                    a.agentview[1][j]=-1
                    a.taskview[0][j]=-1
                    a.taskview[1][j]=-1
            if a.row-2<0:
                for j in range(Agent.view_col):
                    a.agentview[0][j]=-1
                    a.taskview[0][j]=-1
            if a.row+2>Grid.row_num-1:
                for j in range(Agent.view_col):
                    a.agentview[Agent.view_row-1][j]=-1
                    a.taskview[Agent.view_row-1][j]=-1
            if a.row==Grid.row_num-1:
                for j in range(Agent.view_col):
                    a.agentview[Agent.view_row-2][j]=-1
                    a.agentview[Agent.view_row-1][j]=-1
                    a.taskview[Agent.view_row-2][j]=-1
                    a.taskview[Agent.view_row-1][j]=-1
            if a.col==0:
                 for i in range(Agent.view_row):
                    a.agentview[i][0]=-1
                    a.agentview[i][1]=-1
                    a.taskview[i][0]=-1
                    a.taskview[i][1]=-1
            if a.col-2<0:
                for i in range(Agent.view_row):
                    a.agentview[i][0]=-1
                    a.taskview[i][0]=-1
            if a.col+2>Grid.col_num-1:
                for i in range(Agent.view_row):
                    a.agentview[i][Agent.view_col-1]=-1
                    a.taskview[i][Agent.view_col-1]=-1
            if a.col==Grid.col_num-1:
                for i in range(Agent.view_row):
                    a.agentview[i][Agent.view_col-2]=-1
                    a.agentview[i][Agent.view_col-1]=-1
                    a.taskview[i][Agent.view_col-2]=-1
                    a.taskview[i][Agent.view_col-1]=-1
            for b in Agent.AgentList:
                if b.row-a.row+2>0 and b.row-a.row+2<Agent.view_row and b.col-a.col+2>0 and b.col-a.col+2<Agent.view_col:
                    a.agentview[b.row+2-a.row][b.col+2-a.col]=1
            for c in TaskList.TaskList:
                if c.row-a.row+2>0 and c.row-a.row+2<Agent.view_row and c.col-a.col+2>0 and c.col-a.col+2<Agent.view_col:
                    a.taskview[c.row-a.row+2][c.col-a.col+2]=1

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
