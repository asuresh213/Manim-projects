from os import write
from typing_extensions import runtime

from numpy.testing._private.utils import rand
from manimlib import *
import numpy as np
#from manim import *


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

class sqtoline2(Scene):
    def f(self, p):
        for pt in p:
            s = [pt.get_x(), pt.get_y(), 0]
            x = str(abs((s[0]+4)/4))
            y = str(abs((s[1]+2)/4))
            x = x[:min(len(x),len(y))]
            y = y[:min(len(x),len(y))]
            temp = "0."
            first = False 
            second = True
            x_pos = 2
            y_pos = 2
            for i in range(4,len(x)+len(y)):
                if first == True:
                    temp+=x[x_pos]
                    x_pos+=1
                    first = True
                    second = False
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
        line = Line([1,0,0], [5,0,0])
        zero = Tex("0", font_size = 20).move_to([1,-0.2,0])
        one = Tex("1", font_size = 20).move_to([5,-0.2,0])
        self.play(ShowCreation(line), ShowCreation(zero), ShowCreation(one))
        temp_pts = []
        density = 100
        for i in range(density):
            for j in range(density):
                temp_pts.append(Dot([-4+i*(4/density),2-j*(4/density),0]).scale(0.5)) 
        pts = VGroup(*temp_pts)
        self.play(ShowCreation(pts))
        self.wait()
        self.play(pts.animate.set_submobject_colors_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE_D))
        self.wait()
        self.play(ApplyFunction(self.f, pts), run_time = 3)
        self.wait()



class sqtoline3(Scene):
    
    def construct(self):
        self.camera.frame.save_state()
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-3, 10),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-3, 10),
            # The axes will be stretched so as to match the specified
            # height and width
            height=7,
            width=7,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            },
            x_axis_config={
                "include_tip": False,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=5,
            num_decimal_places=1,
        )
        self.add(axes)
        sq = Square(0.5, stroke_width = 2).move_to(axes.c2p(0.5,0.5,0))
        r = ValueTracker(0.25)
        s = ValueTracker(0.25)
        draw_dx = (lambda: Dot(axes.c2p(r.get_value(),0,0),color=BLUE).scale(0.2))
        dx = always_redraw(draw_dx)
        draw_dy = (lambda: Dot(axes.c2p(0,s.get_value(),0), color=RED).scale(0.2))
        dy = always_redraw(draw_dy)
        
        draw_imx = (lambda: Dot(axes.c2p(0.5*((r.get_value())/(np.sqrt(1+(r.get_value())**2)) + 1),0,0), color= BLUE).scale(0.2))
        imx = always_redraw(draw_imx)
        draw_imy = (lambda: Dot(axes.c2p(0,0.5*((s.get_value())/(np.sqrt(1+(s.get_value())**2)) + 1),0), color = RED).scale(0.2))
        imy = always_redraw(draw_imy)
        self.play(ShowCreation(sq))
        self.play(ShowCreation(dx))
        self.play(ShowCreation(dy))
        draw_x = (lambda: Tex("x", font_size = 5).next_to(dx, DOWN, buff = 0.05))
        x_lab = always_redraw(draw_x)
        draw_y = (lambda: Tex("y", font_size = 5).next_to(dy, LEFT, buff = 0.05))
        y_lab = always_redraw(draw_y)
        draw_phi_x = (lambda: Tex("\\phi(x)", font_size = 5).next_to(imx, DOWN, buff = 0.05))
        phi_x_lab = always_redraw(draw_phi_x)
        draw_phi_y = (lambda: Tex("\\phi(y)", font_size = 5).next_to(imy, LEFT, buff = 0.05))
        phi_y_lab = always_redraw(draw_phi_y)

        draw_lx = (lambda: Line(axes.c2p(0.5*((r.get_value())/(np.sqrt(1+(r.get_value())**2))+ 1),0,0), axes.c2p(0.5*((r.get_value())/(np.sqrt(1+(r.get_value())**2)) + 1),0.95,0), stroke_width = 1))
        lx = always_redraw(draw_lx)
        draw_ly = (lambda: Line(axes.c2p(0, 0.5*((s.get_value())/(np.sqrt(1+(s.get_value())**2))+ 1),0), axes.c2p(0.95,0.5*((s.get_value())/(np.sqrt(1+(s.get_value())**2)) + 1),0), stroke_width = 1))
        ly = always_redraw(draw_ly)
        draw_imphi = (lambda: Dot(axes.c2p(0.5*((r.get_value())/(np.sqrt(1+(r.get_value())**2))+ 1), 0.5*((s.get_value())/(np.sqrt(1+(s.get_value())**2))+ 1),0), color=YELLOW).scale(0.15))
        imphi = always_redraw(draw_imphi)
        draw_imphi_lab = (lambda: Tex("\\Phi(x,y)", font_size = 5).next_to(imphi, DL, buff = 0.005))
        imphi_lab = always_redraw(draw_imphi_lab)


        self.play(self.camera.frame.animate.scale(0.20).move_to(imphi))
        def update_curve(mob):
            mob.move_to(imphi.get_center())
        dx2 = dx.copy()
        dy2 = dy.copy()
        self.play(ShowCreation(x_lab), ShowCreation(y_lab))

        self.play(Transform(dx2, imx))
        self.play(Transform(dy2, imy))
        
        self.add(imx)
        self.add(imy)

        self.remove(dx2)
        self.remove(dy2)

        self.play(ShowCreation(phi_x_lab), ShowCreation(phi_y_lab))

        self.play(ShowCreation(lx))
        self.play(ShowCreation(ly))
        
        self.play(ShowCreation(imphi))
        self.play(ShowCreation(imphi_lab))
        self.play(Uncreate(phi_x_lab), Uncreate(phi_y_lab))
        self.camera.frame.add_updater(update_curve)
        self.play(r.animate.set_value(0.75), rate_func = there_and_back, run_time = 0.75)
        self.play(s.animate.set_value(0.75), rate_func = there_and_back, run_time = 0.75)
        for r_ in [5.0, -1.0, 0.25]:
            self.play(r.animate.set_value(r_), s.animate.set_value(0.0-r_), rate_func = smooth, run_time = 2+np.abs(r.get_value()/5))

        self.camera.frame.remove_updater(update_curve)
        self.wait(2)
        self.play(Restore(self.camera.frame))
        
