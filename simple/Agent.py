 class Agent:

    new_id = -1
    AgentList=[]

    @staticmethod
    def __getNewID():
        Agent.new_id += 1
        return Agent.new_id

    def __init__(self, grid, row, col):
        self.id = Agent.__getNewID()
        self.grid=grid
        self.row=row
        self.col=col
        self.score=0

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
