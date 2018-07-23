import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk


UNIT = 40   # pixels
MAZE_H = 5  # grid height
MAZE_W = 10  # grid width


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('Q-Learning')
        self.geometry('{0}x{1}'.format(MAZE_H * 80, MAZE_H * 40))
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_W * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([20, 20])
        # hell
        hell1_center = origin + np.array([UNIT * 2, UNIT*0])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15,
            fill='black')
        # hell
        hell2_center = origin + np.array([UNIT, UNIT*0])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black')
        hell3_center = origin + np.array([UNIT*3, UNIT * 0])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 15, hell3_center[1] - 15,
            hell3_center[0] + 15, hell3_center[1] + 15,
            fill='black')
        hell4_center = origin + np.array([UNIT * 4, UNIT * 0])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 15, hell4_center[1] - 15,
            hell4_center[0] + 15, hell4_center[1] + 15,
            fill='black')
        hell5_center = origin + np.array([UNIT * 5, UNIT * 0])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 15, hell5_center[1] - 15,
            hell5_center[0] + 15, hell5_center[1] + 15,
            fill='black')
        hell6_center = origin + np.array([UNIT * 6, UNIT * 0])
        self.hell6 = self.canvas.create_rectangle(
            hell6_center[0] - 15, hell6_center[1] - 15,
            hell6_center[0] + 15, hell6_center[1] + 15,
            fill='black')
        hell7_center = origin + np.array([UNIT * 7, UNIT * 0])
        self.hell4 = self.canvas.create_rectangle(
            hell7_center[0] - 15, hell7_center[1] - 15,
            hell7_center[0] + 15, hell7_center[1] + 15,
            fill='black')
        hell8_center = origin + np.array([UNIT * 8, UNIT * 0])
        self.hell8 = self.canvas.create_rectangle(
            hell8_center[0] - 15, hell8_center[1] - 15,
            hell8_center[0] + 15, hell8_center[1] + 15,
            fill='black')
        hell9_center = origin + np.array([UNIT * 3, UNIT * 1])
        self.hell9 = self.canvas.create_rectangle(
            hell9_center[0] - 15, hell9_center[1] - 15,
            hell9_center[0] + 15, hell9_center[1] + 15,
            fill='black')
        hell10_center = origin + np.array([UNIT * 7, UNIT * 1])
        self.hell10 = self.canvas.create_rectangle(
            hell10_center[0] - 15, hell10_center[1] - 15,
            hell10_center[0] + 15, hell10_center[1] + 15,
            fill='black')
        hell111_center = origin + np.array([UNIT * 1, UNIT * 3])
        self.hell111 = self.canvas.create_rectangle(
            hell111_center[0] - 15, hell111_center[1] - 15,
            hell111_center[0] + 15, hell111_center[1] + 15,
            fill='black')
        hell112_center = origin + np.array([UNIT * 2, UNIT * 3])
        self.hell112 = self.canvas.create_rectangle(
            hell112_center[0] - 15, hell112_center[1] - 15,
            hell112_center[0] + 15, hell112_center[1] + 15,
            fill='black')
        hell113_center = origin + np.array([UNIT * 4, UNIT * 3])
        self.hell113 = self.canvas.create_rectangle(
            hell113_center[0] - 15, hell113_center[1] - 15,
            hell113_center[0] + 15, hell113_center[1] + 15,
            fill='black')
        hell114_center = origin + np.array([UNIT * 5, UNIT * 3])
        self.hell114 = self.canvas.create_rectangle(
            hell114_center[0] - 15, hell114_center[1] - 15,
            hell114_center[0] + 15, hell114_center[1] + 15,
            fill='black')
        hell115_center = origin + np.array([UNIT * 4, UNIT * 4])
        self.hell115 = self.canvas.create_rectangle(
            hell115_center[0] - 15, hell115_center[1] - 15,
            hell115_center[0] + 15, hell115_center[1] + 15,
            fill='black')
        hell116_center = origin + np.array([UNIT * 5, UNIT * 4])
        self.hell116 = self.canvas.create_rectangle(
            hell116_center[0] - 15, hell116_center[1] - 15,
            hell116_center[0] + 15, hell116_center[1] + 15,
            fill='black')
        hell117_center = origin + np.array([UNIT * 7, UNIT * 3])
        self.hell117 = self.canvas.create_rectangle(
            hell117_center[0] - 15, hell117_center[1] - 15,
            hell117_center[0] + 15, hell117_center[1] + 15,
            fill='black')

        # create oval
        oval_center = origin + np.array([UNIT * 9, UNIT*0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow')

        # create red rect
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.10)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')
        # return observation
        return self.canvas.coords(self.rect)

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 2:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 3:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 4:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent


    def render(self):
        time.sleep(0.1)
        self.update()


def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            env.step(a)


if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()