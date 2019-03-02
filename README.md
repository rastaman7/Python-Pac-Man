# Python-Pac-Man
The newest version of this project is in the grid_3x3 file.

In this project, agents will try to collect items on its own.
Method used in this project is Q-learning.
In app_rand.py, the agent moves randomly in the given grid, whereas, in app_notrand.py, the agent moves according to what it learned before.


1. Initialize the size of the grid by opening the Grid.py and changing the row_num and col_num.
2. In the 12th and 13th line of app_rand.py and app_notrand.py, place the agent and the task by changing the numbers in the          brackets.
3. In line 8 and 9 in the Agents.py, change the number of view_row and view_col to 3, 5, 7... This is the size of the grid that the agents see(the agent is in the middle).
4. In line 22 of app_rand.py and line 23 of app_notrand.py, change the number next to the while loop. this will allow you to change the number of times the agent is allowed to move.
run 
python3 app_rand.py
python3 app_notrand.py
to see this project.

This project shows how the performance of the agents get better with more moves and bigger views.
