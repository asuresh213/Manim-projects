#import pygame
import math
import re
import random
import time
import numpy as np
from os import write
from manimlib import *

class LSystem:
    def __init__(self, axiom, rules, x, y, length, dtheta):
        self.axiom = axiom
        self.sentence = axiom
        self.rules = rules
        self.xInit = x
        self.yInit = y
        self.x = x
        self.y = y
        self.theta = 0
        self.length = length
        self.dtheta = dtheta
        self.stack = []
        self.pts = [[self.x, self.y, 0.0]]

    def generate(self):
        self.x = self.xInit
        self.y = self.yInit
        self.theta = 0
        self.length *= 0.30
        newSent = ''
        for char in self.sentence:
            match = False
            for rule in self.rules:
                if (rule['in'] == char):
                    newSent += rule['out']
                    match = True
                    break
            if (not match):
                newSent += char
        self.sentence = newSent

    def printSent(self):
        print(self.sentence)

    def draw(self):
        color = 0
        dcolor = 255 / len(self.sentence)
        for char in self.sentence:
            # print(char)
            if (char == 'F' or char == 'G' or char == 'A' or char == 'B'):
                x2 = self.x + self.length * math.cos(self.theta)
                y2 = self.y + self.length * math.sin(self.theta)
                #pygame.draw.line(screen, (color, 255 - color, 100 + color / 255, 100),
                                 #(self.x, self.y), (x2, y2))
                self.x = x2
                self.y = y2
                self.pts.append(np.array([float(self.x), float(self.y),0.0]))

            elif (char == '+'):
                self.theta += self.dtheta
            elif (char == '-'):
                self.theta -= self.dtheta
            elif (char == '['):
                self.stack.append(
                    {'x': self.x, 'y': self.y, 'theta': self.theta})
            elif (char == ']'):
                dict = self.stack.pop()
                self.x = dict['x']
                self.y = dict['y']
                self.theta = dict['theta']
            color += dcolor


class ArrowHead(Scene):
    def construct(self):
        systems = []
        with open('tree.txt') as text:
            for line in text:
                stringList = re.split(',|\n', line)
                axiom = stringList[1]
                angle = math.radians(int(stringList[2]))
                length = int(stringList[3])
                x, y = int(stringList[4]), int(stringList[5])
                rulesList = stringList[6].split()
                rules = []
                for rule in rulesList:
                    rules.append({
                        'in': rule.split('->')[0],
                        'out': rule.split('->')[1]
                    })
                systems.append(LSystem(axiom, rules, x, y, length, angle))

        print(len(systems))
        curr = systems[7]
        ord = -1
        path = []
        max_order = 4
        colors = [PURPLE_E, BLUE_E, BLUE_D, GREEN_D, YELLOW_E, ORANGE, RED_E]
        for i in range(max_order):
            ord += 1
            curr.generate()
            curr.draw()
            path.append(np.array(curr.pts))
            curr.pts = [[x, y, 0.0]]


        #curve = VMobject()
        #curve.set_points_as_corners([[-3,0,0], [3,0,0]]).move_to([0,-2,0], aligned_edge=ORIGIN)
        #colors = color_gradient(colors, len(curve.get_points()))
        #curve.set_color_by_gradient(colors)
        #self.play(ShowCreation(curve))

        #curve = VMobject()
        #curve.set_points_as_corners([*path[-1]])
        #self.play(ShowCreation(curve), run_time=4)

        curve = VMobject()
        if(i%2==0):
            curve.set_points_as_corners([*path[-1]])
            #curve.rotate(angle)
            curve.move_to([0,-2,0], aligned_edge=BOTTOM)
        else:
            curve.set_points_as_corners([*path[-1]]).move_to([0,-2,0], aligned_edge=BOTTOM)
        colors = color_gradient(colors, len(curve.get_points()))
        curve.set_color_by_gradient(colors)
        self.play(ShowCreation(curve), run_time=4)
        self.wait(0.5)
