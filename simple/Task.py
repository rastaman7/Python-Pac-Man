class Task:
    def __init__(self, grid, row, col):
        self.grid=grid
        self.row=row
        self.col=col

        self.grid.cells[row][col]=2

    def removeItem(self):
        self.grid.cells[self.row][self.col]=0
        del self
