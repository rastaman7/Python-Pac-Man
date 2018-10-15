 Agent:
    def __init__(self, grid, row, col):
        self.grid=grid
        self.row=row
        self.col=col

        self.grid.cells[row][col]=1

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
           class self.grid.cells[self.row][self.col+1]=0
        else:
            print("unable to move left")

    def move_right(self):
        if self.col<self.grid.col_num-1 and self.grid.cells[self.row][self.col+1] != 1:
            self.col=self.col+1
            self.grid.cells[self.row][self.col]=1
            self.grid.cells[self.row][self.col-1]=0
        else:
            print("unable to move right")
