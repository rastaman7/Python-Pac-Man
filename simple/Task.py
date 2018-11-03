from TaskList import TaskList

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

    def removeItem(self):
        self.grid.cells[self.row][self.col]=0
        del self
