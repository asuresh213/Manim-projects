from os import write
from manimlib import *
import numpy as np


class Hilbert(Scene):
    def construct(self):
        width = 6
        l = 3
        colors = [PURPLE_E, BLUE_E, BLUE_D, GREEN_D, YELLOW_E, ORANGE, RED_E]
        text = (Text("Hilbert Curve").scale(0.25)).to_edge(UP)
        self.play(Write(text))
        order = 7
        N = 2**order
        total = N*N

        ul = Dot(np.array([0, 0,0])*width)
        ur = Dot(np.array([0,-1,0])*width)
        bl = Dot(np.array([1,-1,0])*width)
        br = Dot(np.array([1,0,0])*width)
        pts = VGroup(ul,ur, bl,br).to_corner(UL)
        orig = Dot(pts.get_center())


        path = np.zeros((total,3))
        #print(len(path))
        l = width/N
        lines = []
        for i in range(total):
            path[i] = self.hilbert(i, order, total)
            path[i] = path[i]*l
        curve = VMobject()
        curve.set_points_as_corners([*path])
        curve.move_to([0,0,0], aligned_edge=ORIGIN)
        colors = color_gradient(colors, len(curve.get_points()))
        curve.set_color_by_gradient(colors)
        self.play(ShowCreation(curve), run_time=10)
        self.wait(0.5)

    def hilbert(self, i, order, total):
        points = np.array([[0,0,0], [0,-1,0], [1,-1,0],[1,0,0]])

        index = i&3
        v = points[index]
        for j in range(1,order):
            i = i>>2
            index = i&3
            l = 2**j
            if(index == 0):
                temp = v[0]
                v[0] = -v[1]
                v[1] = -temp
            elif(index == 1):
                v[1] -= l
            elif(index == 2):
                v[0]+= l
                v[1]-= l
            elif(index == 3):
                temp = l-1-v[0]
                v[0] = l-1+v[1]
                v[1] = -temp
                v[0] += l


        return v
