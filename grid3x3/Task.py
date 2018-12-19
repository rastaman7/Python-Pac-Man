from TaskList import TaskList
from Grid import Grid
import random

class Task:
    new_id = -1

    @staticmethod
    def __getNewID():
        Task.new_id += 1
        return Task.new_id

    def __init__(self, grid, row, col):
        self.id = Task.__getNewID()
        self.grid=grid
        self.row=row
        self.col=col

        self.grid.cells[row][col]=1
        TaskList(self)

    def removeTask(self):
        self.grid.cells[self.row][self.col]=0
        TaskList.TaskList.remove(self)
        del self

    def crateTask(grid1, grid2):
        while True:
            r=random.randint(0,Grid.row_num-1)
            c=random.randint(0,Grid.col_num-1)
            if grid1.cells[r][c]==0 and grid2.cells[r][c]==0:
                Task(grid2,r,c)
                break

    def moveTask(self, newrow, newcol):
        self.row=newrow
        self.col=newcol
