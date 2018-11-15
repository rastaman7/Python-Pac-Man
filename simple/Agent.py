from Grid import Grid
from TaskList import TaskList

class Agent:

    new_id = -1
    AgentList=[]

    @staticmethod
    def __getNewID():
        Agent.new_id += 1
        return Agent.new_id

    def agentView():
        for a in Agent.AgentList:
            a.view=[[0,0,0],[0,0,0],[0,0,0]]
            if a.row==0:
                a.view[0]=[-1,-1,-1]
            if a.row==Grid.row_num-1:
                a.view[2]=[-1,-1,-1]
            if a.col==0:
                a.view[0][0]=-1
                a.view[1][0]=-1
                a.view[2][0]=-1
            if a.col==Grid.col_num-1:
                a.view[0][2]=-1
                a.view[1][2]=-1
                a.view[2][2]=-1
            for b in Agent.AgentList:
                if b.row-a.row+1>=0 and b.row-a.row+1<=2:
                    if b.col-a.col+1>=0 and b.col-a.col+1<=2:
                        a.view[b.row-a.row+1][b.col-a.col+1]=-1
            for c in TaskList.TaskList:
                if c.row-a.row+1>=0 and c.row-a.row+1<=2:
                    if c.col-a.col+1>=0 and c.col-a.col+1<=2:
                        a.view[c.row-a.row+1][c.col-a.col+1]=1

    def __init__(self, grid, row, col):
        self.id = Agent.__getNewID()
        self.grid=grid
        self.row=row
        self.col=col
        self.score=0
        self.view=[[0,0,0],[0,0,0],[0,0,0]]

        self.grid.cells[row][col]=1
        Agent.AgentList.append(self)

    def move_up(self):
        if self.row>0 and self.grid.cells[self.row-1][self.col] != 1:
            self.row=self.row-1
            self.grid.cells[self.row][self.col]=1
            self.grid.cells[self.row+1][self.col]=0
        else:
            print("unable to move up")

    def move_down(self):
        if self.row<self.grid.row_num-1 and self.grid.cells[self.row+1][self.col] != 1:
            self.row=self.row+1
            self.grid.cells[self.row][self.col]=1
            self.grid.cells[self.row-1][self.col]=0
        else:
            print("unable to move down")

    def move_left(self):
        if self.col>0 and self.grid.cells[self.row][self.col-1] != 1:
            self.col=self.col-1
            self.grid.cells[self.row][self.col]=1
            self.grid.cells[self.row][self.col+1]=0
        else:
            print("unable to move left")

    def move_right(self):
        if self.col<self.grid.col_num-1 and self.grid.cells[self.row][self.col+1] != 1:
            self.col=self.col+1
            self.grid.cells[self.row][self.col]=1
            self.grid.cells[self.row][self.col-1]=0
        else:
            print("unable to move right")

    def earn_score(self):
        self.score=self.score+1

    def get_score(self):
        return self.score

    def printView(self):
        for i in range(3):
            print(self.view[i])
        print("-------")
