#from manimlib.scene.moving_camera_scene import MovingCameraScene
from os import write
from typing_extensions import runtime

from numpy.testing._private.utils import rand
from manimlib import *
import numpy as np

def line_eq(r, x):
    if r == 0:
        return 0
    else: 
        return (-1/r)*x + 1

def circ_eq(x):
    return 1-np.sqrt(1-x**2)




class Rtosegment(Scene):
    def construct(self):
        r = ValueTracker(-2)
        grid = NumberPlane((-10,10),(-5,5))
        center = [0,1,0]
        circ = Arc(PI,PI)
        circ.move_arc_center_to(center)
        point = Dot([0,1,0]).set_fill(YELLOW)
        x_int = (r.get_value())/(np.sqrt(1+(r.get_value())**2)) 
        y_int = line_eq(r.get_value(), x_int)
        intersection_dot = (lambda: (Dot([(r.get_value())/(np.sqrt(1+(r.get_value())**2)), line_eq(r.get_value(), (r.get_value())/(np.sqrt(1+(r.get_value())**2))), 0]).set_color(RED_B)).scale(0.5))
        intersection = always_redraw(intersection_dot)
        draw_line = (lambda: Line(point, [r.get_value(),0,0], stroke_color=YELLOW, stroke_width=3))
        line = always_redraw(draw_line)
        draw_vert_line = (lambda: Line([(r.get_value())/(np.sqrt(1+(r.get_value())**2)), line_eq(r.get_value(), (r.get_value())/(np.sqrt(1+(r.get_value())**2))), 0], [(r.get_value())/(np.sqrt(1+(r.get_value())**2)),0,0], stroke_color=RED_B, stroke_width = 3))
        vert_line = always_redraw(draw_vert_line)
        #draw_hor_line = (lambda: Line([-1,0,0], [(r.get_value())/(np.sqrt(1+(r.get_value())**2)),0,0], stroke_width = 3, stroke_color = RED_B) )
        #hor_line = always_redraw(draw_hor_line)
        draw_x_val = (lambda: (Dot([r.get_value(),0,0]).set_color(YELLOW)).scale(0.5))
        x_val = always_redraw(draw_x_val)
        draw_input_label = (lambda: TexText("$x = {:.2f}$".format(r.get_value()), font_size = 14).next_to(x_val,DOWN))
        input_label = always_redraw(draw_input_label)
        draw_phi_val = (lambda: (Dot([(r.get_value())/(np.sqrt(1+(r.get_value())**2)),0,0]).set_color(RED)).scale(0.5))
        phi_val = always_redraw(draw_phi_val)
        draw_output_label = (lambda: TexText("$\\varphi(x) = {:.5f}$".format((r.get_value())/(np.sqrt(1+(r.get_value())**2))), font_size = 14).next_to(phi_val,DOWN))
        output_label = always_redraw(draw_output_label)
        self.play(ShowCreation(grid), run_time = 2, lag_ratio = 0.1)
        self.play(ShowCreation(circ))
        self.play(ShowCreation(point))
        self.play(ShowCreation(line))
        self.play(ShowCreation(x_val))
        self.play(ShowCreation(input_label))
        self.play(ShowCreation(intersection))
        self.play(ShowCreation(vert_line))
        #self.play(ShowCreation(hor_line))
        self.play(ShowCreation(phi_val))
        self.play(ShowCreation(output_label))
        self.wait(1) 
        
        Inj_text = TexText("$\\varphi$ is injective", font_size = 25).to_edge(UP)
        self.play(ShowCreation(Inj_text))
        for r_ in [-2.2, -1.8]:
            self.play(r.animate.set_value(r_), rate_func=there_and_back, run_time = 2)
        self.play(r.animate.set_value(4), run_time = 2)
        for r_ in [3.8, 4.2]:
            self.play(r.animate.set_value(r_), rate_func=there_and_back, run_time = 2)

        self.play(Uncreate(output_label))
        self.play(Uncreate(input_label))
        self.play(Uncreate(Inj_text))
        self.play(Uncreate(phi_val))
        self.play(Uncreate(vert_line))
        self.play(Uncreate(intersection))
        self.play(Uncreate(line))
        self.play(Uncreate(x_val))
        self.wait(1)
        draw_input_label = (lambda: TexText("$\\varphi^{-1}(t)$", font_size = 14).next_to(x_val,DOWN))
        input_label = always_redraw(draw_input_label)
        draw_output_label = (lambda: TexText("$t$", font_size = 14).next_to(phi_val,DOWN))
        output_label = always_redraw(draw_output_label)
        Surj_text = TexText("$\\varphi$ is surjective", font_size = 25).to_edge(UP)
        self.play(ShowCreation(Surj_text))
        self.play(ShowCreation(phi_val))
        self.play(ShowCreation(output_label))
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(line))
        self.play(ShowCreation(x_val))
        self.play(ShowCreation(input_label))
        self.play(r.animate.set_value(-3.5), run_time = 2)
        self.play(r.animate.set_value(-250), rate_func = there_and_back, run_time=4)
        self.play(r.animate.set_value(3.5), run_time = 2)
        self.play(r.animate.set_value(250), run_time = 4)
        #self.wait(2)
        self.play(Uncreate(Surj_text))
        self.play(Uncreate(output_label))
        self.play(Uncreate(phi_val))
        self.play(Uncreate(vert_line))
        self.play(Uncreate(line))
        self.play(Uncreate(input_label))
        self.play(Uncreate(x_val))


class sqtoline(Scene):
    def f(self, p):
        for pt in p:
            s = [pt.get_x(), pt.get_y(), 0]
            x = str(abs((s[0]+4)/4))
            y = str(abs((s[1]+2)/4))
            x = x[:min(len(x),len(y))]
            y = y[:min(len(x),len(y))]
            temp = "0."
            first = True 
            second = False
            x_pos = 2
            y_pos = 2
            for i in range(4,len(x)+len(y)):
                if first == True:
                    temp+=x[x_pos]
                    x_pos+=1
                    first = False
                    second = True
                elif second == True:
                    temp += y[y_pos]
                    y_pos+=1
                    first = True
                    second = False
            #print(x,y,temp)
            temp = (1+4*float(temp))
            pt.move_to([temp, 0, 0])
            pt.scale(0.25)
        return p

    def construct(self):
        sq = Square(4).move_to([-2,0,0])
        self.play(ShowCreation(sq))
        x_coord = ValueTracker(0)
        y_coord = ValueTracker(0)
        draw_sq_pt = (lambda: Dot([-4+4*x_coord.get_value(),-2+4*y_coord.get_value(),0], color=YELLOW).scale(0.5))
        sq_pt = always_redraw(draw_sq_pt)
        self.play(ShowCreation(sq_pt))
        draw_pt_label = (lambda: Tex("(", "{:.5f}".format(x_coord.get_value()), ",", "{:.5f}".format(y_coord.get_value()), ")", font_size = 14).next_to(sq_pt, DOWN))
        pt_label = always_redraw(draw_pt_label)
        self.play(ShowCreation(pt_label))
        self.play(Uncreate(pt_label))
        #self.play(x_coord.animate.set_value(0.857437), y_coord.animate.set_value(0.375645))
        #draw_pt_label = (lambda: Tex("(", "{:.5f}".format(x_coord.get_value()), ",", "{:.5f}".format(y_coord.get_value()), ")", font_size = 14).next_to(sq_pt, DOWN))
        #pt_label = always_redraw(draw_pt_label)
        #self.play(ShowCreation(pt_label))
        #self.play(Uncreate(pt_label))
        self.play(x_coord.animate.set_value(1.0000), y_coord.animate.set_value(1.0000))
        draw_pt_label = (lambda: Tex("(", "{:.5f}".format(x_coord.get_value()), ",", "{:.5f}".format(y_coord.get_value()), ")", font_size = 14).next_to(sq_pt, UP))
        pt_label = always_redraw(draw_pt_label)
        self.play(ShowCreation(pt_label))
        self.play(Uncreate(pt_label))
        self.play(x_coord.animate.set_value(0.65743), y_coord.animate.set_value(0.57564))
        draw_pt_label = (lambda: Tex("(", "{:.5f}".format(x_coord.get_value()), ",", "{:.5f}".format(y_coord.get_value()), ")", font_size = 14).next_to(sq_pt, DOWN))
        pt_label = always_redraw(draw_pt_label)
        self.play(ShowCreation(pt_label))
        self.wait()
        x_y_val_text = VGroup(Tex("0.", "6", "5", "7", "4", "3"), Tex("0.", "5","7","5","6","4"))
        x_y_val_text.arrange(DOWN)
        x_y_val_text.move_to([3,3,0])
        self.play(TransformMatchingTex(pt_label, x_y_val_text, path_arc = 90*DEGREES))
        target_text = Tex("0.", "6", "5", "5", "7", "7", "5", "4", "6", "3", "4").next_to(x_y_val_text, 1.5*DOWN)
        x_y_val_text_2 = x_y_val_text.copy()   
        self.play(TransformMatchingShapes(x_y_val_text_2, target_text))
        #for i in range(11):
            #if(i%2 == 0):
                #self.play(x_y_val_text[1][int(i/2)].animate.set_color(YELLOW), target_text[i].animate.set_color(YELLOW))
        
        line = Line([1,0,0], [5,0,0])
        zero = Tex("0", font_size = 20).move_to([1,-0.2,0])
        one = Tex("1", font_size = 20).move_to([5,-0.2,0])
        pt = (Dot([3.6231018536,0,0]).set_color(YELLOW)).scale(0.5)
        pt_text = Tex("0.6557754634", font_size=25).next_to(pt, DOWN)
        self.play(ShowCreation(line), ShowCreation(zero), ShowCreation(one))
        sq_pt2 = sq_pt.copy()
        self.play(Transform(sq_pt2, pt, path_arc=90*DEGREES), Uncreate(sq_pt))
        target_text_2 = target_text.copy()
        self.play(Transform(target_text_2, pt_text))
        self.wait(2)
        self.play(Uncreate(x_y_val_text))
        #self.play(Uncreate(x_y_val_text_2))
        self.play(Uncreate(target_text))
        self.play(Uncreate(target_text_2))
        #self.play(Uncreate(pt_text))
        self.play(Uncreate(sq_pt2))
        temp_pts = []
        density = 50
        for i in range(density):
            for j in range(density):
                temp_pts.append(Dot([-4+i*(4/density),2-j*(4/density),0]).scale(0.5)) 
        pts = VGroup(*temp_pts)
        self.play(ShowCreation(pts))
        self.wait()
        self.play(pts.animate.set_submobject_colors_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE_D))
        self.wait()
        self.play(ApplyFunction(self.f, pts))
        self.wait()
                


class sqtoline1(Scene):
    def construct(self):
        sq = Square(4).move_to([-2,0,0])
        self.play(ShowCreation(sq))
        x_coord = ValueTracker(0)
        y_coord = ValueTracker(0)
        draw_sq_pt = (lambda: Dot([-4+4*x_coord.get_value(),-2+4*y_coord.get_value(),0], color=YELLOW).scale(0.5))
        sq_pt = always_redraw(draw_sq_pt)
        self.play(ShowCreation(sq_pt))
        draw_pt_label = (lambda: Tex("(", "{:.5f}".format(x_coord.get_value()), ",", "{:.5f}".format(y_coord.get_value()), ")", font_size = 14).next_to(sq_pt, DOWN))
        pt_label = always_redraw(draw_pt_label)
        self.play(ShowCreation(pt_label))
        self.play(Uncreate(pt_label))
        self.play(x_coord.animate.set_value(1.0000), y_coord.animate.set_value(1.0000))
        draw_pt_label = (lambda: Tex("(", "{:.5f}".format(x_coord.get_value()), ",", "{:.5f}".format(y_coord.get_value()), ")", font_size = 14).next_to(sq_pt, UP))
        pt_label = always_redraw(draw_pt_label)
        self.play(ShowCreation(pt_label))
        self.play(Uncreate(pt_label))
        self.play(x_coord.animate.set_value(0.65743), y_coord.animate.set_value(0.57564))
        draw_pt_label = (lambda: Tex("(", "{:.5f}".format(x_coord.get_value()), ",", "{:.5f}".format(y_coord.get_value()), ")", font_size = 14).next_to(sq_pt, DOWN))
        pt_label = always_redraw(draw_pt_label)
        self.play(ShowCreation(pt_label))
        self.wait()
        x_y_val_text = VGroup(Tex("0.", "6", "5", "7", "4", "3"), Tex("0.", "5","7","5","6","4"))
        x_y_val_text.arrange(DOWN)
        x_y_val_text.move_to([3,3,0])
        self.play(TransformMatchingShapes(pt_label, x_y_val_text, path_arc = 90*DEGREES))
        target_text = Tex("0.", "6", "5", "5", "7", "7", "5", "4", "6", "3", "4").next_to(x_y_val_text, 1.5*DOWN)
        x_y_val_text_2 = x_y_val_text.copy()   
        self.play(TransformMatchingShapes(x_y_val_text_2, target_text))
        line = Line([1,0,0], [5,0,0])
        zero = Tex("0", font_size = 20).move_to([1,-0.2,0])
        one = Tex("1", font_size = 20).move_to([5,-0.2,0])
        pt = (Dot([3.6231018536,0,0]).set_color(YELLOW)).scale(0.5)
        pt_text = Tex("0.6557754634", font_size=25).next_to(pt, DOWN)
        self.play(ShowCreation(line), ShowCreation(zero), ShowCreation(one))
        sq_pt2 = sq_pt.copy()
        self.play(Transform(sq_pt2, pt, path_arc=90*DEGREES), Uncreate(sq_pt))
        target_text_2 = target_text.copy()
        self.play((target_text_2.animate.move_to(pt_text.get_center())).scale(0.5))
        self.wait(2)

