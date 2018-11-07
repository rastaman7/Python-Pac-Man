from Agent import Agent
from Task import Task
from TaskList import TaskList

class Score:

    def checkScore(agent, taskgrid):
        if taskgrid.cells[agent.row][agent.col]==1:
            for b in TaskList.TaskList:
                if b.row==agent.row and b.col==agent.col:
                    agent.earn_score()
                    b.removeTask()
