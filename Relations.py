from manimlib.imports import *
import numpy as np

class Relations_Whattheyare(Scene):
    def construct(self):
        title = TextMobject("Relations").to_edge(UP)
        motiv = TextMobject(r"Most situations in mathematics can be discribed by relations between objects")
        motiv.scale(0.75)
        motiv.to_corner(UL, buff = 1).shift(DOWN)
        defn = TextMobject(r"A relation is simply a correspondence between two sets of objects").next_to(motiv, DOWN, buff = 0.1).scale(0.75)
        ex = TextMobject(r"\textbf{Example:} Consider the following table of temperatures in different places in Georgia, and how we can view that as a relation where each city is `related' to its temperature").next_to(defn, DOWN, buff = 0.1).scale(0.5)
        tab = TexMobject(r"\begin{tabular} { || c | c ||} \hline Atlanta & 52 \\ Decatur & 50 \\ Macon & 55 \\ Suwanee & 50 \\ \hline \end{tabular}").to_corner(DL, buff = 0.5)
        dom = Ellipse(width = 2, height = 3).to_edge(RIGHT, buff = 5).shift(2*DOWN)
        rng = Ellipse(width = 1, height = 3).to_edge(RIGHT, buff = 2).shift(2*DOWN)
        DomText = TexMobject("Atlanta", "\\\ ", "Decatur", "\\\ ", "Macon", "\\\ ", "Suwanee").move_to(dom.get_center()).scale(0.60)
        RngText = TexMobject("52", "\\\ ", "50", "\\\ ", "55").move_to(rng.get_center()).scale(0.80)
        connections = VGroup(Arrow(DomText[0], RngText[0], stroke_width = 1, tip_length = 0.15), 
                            Arrow(DomText[2], RngText[2], stroke_width = 1, tip_length=0.15), 
                            Arrow(DomText[4], RngText[4], stroke_width = 1,tip_length = 0.15), 
                            Arrow(DomText[6], RngText[2], stroke_width = 1, tip_length = 0.15))
        
        iff = TexMobject(r"\Leftrightarrow").move_to(dom.get_center()).shift(2*LEFT)
        self.play(Write(title))
        self.wait()
        self.play(Write(motiv))
        self.wait()
        self.play(Write(defn))
        self.wait()
        self.play(Write(ex))
        self.wait()
        self.play(ShowCreation(tab))
        self.wait()
        self.play(FadeInFromDown(iff))
        self.wait()
        self.play(ShowCreation(dom), ShowCreation(rng))
        self.wait()
        self.play(FadeIn(DomText), FadeIn(RngText))
        self.wait()
        self.play(ShowCreation(connections))
        self.wait()


class DomRng(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : -4,
        "x_max" : 3,
        "x_min" : -3,
        "y_tick_frequency" : 2,
        "axes_color" : BLUE,
        "x_axis_label" : "$x$",
        "y_axis_label" : "$y$",
        "graph_origin" : np.array((3,-1.5,0))
    }
    def construct(self):
        title = TextMobject("Relations Terminologies").to_edge(UP)
        text = TextMobject("Consider the relation $f$ where a real number $x$, is related to a real number $y$ if $y=x^2$").next_to(title, DOWN, buff = 0.5).scale(0.5)
        dom = Ellipse(width = 1, height = 3).shift(4*LEFT + 0.80*DOWN)
        codom = Ellipse(width = 1, height = 3).next_to(dom, RIGHT, buff = 1)
        rng = Ellipse(width = 0.5, height = 1.5).move_to(codom.get_center()).shift(0.5*UP)
        domtext = TexMobject("\\vdots \\\ -2 \\\ -1 \\\ 0 \\\ 1 \\\ 2 \\\ \\vdots").move_to(dom.get_center()).scale(0.45).shift(0.05*LEFT)
        rngtext = TexMobject("0 \\\ 1 \\\ 4 \\\ \\vdots").move_to(rng.get_center()).scale(0.35)
        codomtext = TexMobject(r"-1 \\ -4").next_to(rng, DOWN, buff = 0).scale(0.45)
        toplin = Line(start = dom.get_top(), end = rng.get_top())
        botlin = Line(start = dom.get_bottom(), end = rng.get_bottom())
        domname = TextMobject("Domain").next_to(dom, DOWN, buff= 0.1).scale(0.5)
        codomname = TextMobject("Codomain").next_to(codom, DOWN, buff= 0.1).scale(0.5)
        rngname = TextMobject("Range").next_to(codom, RIGHT, buff= 0.1).scale(0.5)
        mapname = TexMobject("f").next_to(toplin, DOWN, buff = 0.1).scale(0.5)
        point = Arrow(rngname, rng, buff = 0.1, stroke_width =1, tip_length = 0.15)
        alg = TextMobject("Set-Theoretic").next_to(dom, UP, buff = 0.5).shift(RIGHT).scale(0.5)
        gr = TextMobject("Graphical").next_to(alg, RIGHT, buff = 4.5).scale(0.5)
        self.play(FadeInFromDown(title))
        self.wait()
        self.play(Write(text))
        self.wait()
        self.play(Write(alg), Write(gr))
        self.play(ShowCreation(dom)) 
        self.wait()
        self.play(ShowCreation(domtext))
        self.wait()
        self.play(ShowCreation(codom), ShowCreation(rng), Write(rngtext), Write(codomtext))
        self.wait()
        self.play(ShowCreation(botlin), ShowCreation(toplin))
        self.wait()
        self.play(Write(domname), Write(codomname), Write(rngname), Write(mapname), ShowCreation(point))
        self.wait()
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)
        self.play(ShowCreation(graph),run_time = 2)
        self.wait()
        ls1 = np.array((0,0,0))
        le1 = np.array((-1.5,0,0))
        le2 = np.array((1.5,0,0))
        le3 = np.array((0, 0.5, 0))
        le4 = np.array((0,1.5,0))
        domline1 = Arrow(start = ls1, end = le1).next_to(graph, DOWN, buff = 1.5).shift(1.40*LEFT)
        domline2 = Arrow(start = ls1, end = le2).next_to(graph, DOWN, buff = 1.5).shift(1.40*RIGHT)
        domname2 = domname.copy().next_to(graph, DOWN, buff = 1.5).scale(1.5)
        rngline1 = Line(start = ls1, end = le3).next_to(graph, RIGHT, buff = 0.25).shift(0.70*DOWN)
        rngname2 = rngname.copy().rotate(PI/2).next_to(rngline1, UP, buff = 0.1)
        le5 = np.array((5.72, 0, 0))
        rngline2 = Arrow(start = rngname2.get_top() + np.array((0, 0.01, 0)), end = rngname2.get_top() + np.array((0, 1.1, 0)))
        codomname2 = codomname.copy().rotate(PI/2).next_to(rngname2, RIGHT, buff = 0.1).shift(0.5*DOWN)
        codomline1 = Arrow(start = codomname2.get_top() + np.array((0, 0.01, 0)), end = codomname2.get_top() + np.array((0, 1.1, 0)))
        codomline2 = Arrow(start = codomname2.get_bottom() + np.array((0, -0.01, 0)), end = codomname2.get_bottom() + np.array((0, -1.1, 0)))
        self.play(ShowCreation(domline1), ShowCreation(domline2), Write(domname2), ShowCreation(rngline1), Write(rngname2), ShowCreation(rngline2), ShowCreation(codomname2), ShowCreation(codomline1), ShowCreation(codomline2))
        self.wait(4)
    
    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = -3
        end_label_x = 3
        step_x = 1
        #   For y
        init_label_y = -4
        end_label_y = 10
        step_y = 6
        # Position of labels
        #   For x
        self.x_axis.scale(0.5).shift(0.22*RIGHT)
        self.y_axis.scale(0.5)
        self.y_axis.shift(0.65*DOWN + 0.15*RIGHT)
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y,
                                        step_y
                                    ))
        self.play(ShowCreation(self.x_axis),ShowCreation(self.y_axis))




class Functions(Scene):
    def construct(self):
        title = TextMobject("Function").to_edge(UP)
        intro_text = TextMobject("Consider the function $f(x) = x^2 + 2x + 3$ and imagine a machine" ).next_to(title, DOWN, buff = 0.1).scale(0.75)
        exp_text = TextMobject("Takeaway: The machine knows to do only one thing -- replace the variable $x$ with whatever input it gets").to_edge(DOWN).scale(0.5)
        body = Rectangle(height = 3, width = 5)
        funnel1 = (Square().scale(0.5)).next_to(body, UP, buff = 0)
        mouth1 = Rectangle(width = 1.50, height = 0.35).next_to(funnel1, UP, buff = 0)
        funnel2 = ((Square().scale(0.5)).next_to(body, RIGHT, buff = 0)).shift(0.75*DOWN)
        funnel3 = ((Rectangle(width = 0.75, height = 1.50)).next_to(funnel2, RIGHT, buff = 0)).shift(0.50*DOWN)
        mouth2 = Rectangle(width = 1, height = 0.25).next_to(funnel3, DOWN, buff = 0)
        machine = Polygon(
            mouth1.point_from_proportion(0), 
            funnel1.point_from_proportion(0),
            funnel1.point_from_proportion(0.75),
            body.point_from_proportion(0),
            body.point_from_proportion(0.75),
            body.point_from_proportion(0.5),
            funnel2.point_from_proportion(0.75),
            funnel2.point_from_proportion(0.50),
            funnel3.point_from_proportion(0.75),
            mouth2.point_from_proportion(0.75),
            mouth2.point_from_proportion(0.5),
            funnel3.point_from_proportion(0.50),
            funnel3.point_from_proportion(0.25),
            funnel2.point_from_proportion(0),
            body.point_from_proportion(0.25),
            funnel1.point_from_proportion(0.5),
            funnel1.point_from_proportion(0.25),
            mouth1.point_from_proportion(0.25)
            )
        #self.add(body, funnel1, mouth1, funnel2, funnel3, mouth2)
        inp = TexMobject("2", "1", "\\clubsuit", "x^2").next_to(machine.get_top(), UP, buff = -1).shift(0.80*LEFT)
        inp[0].shift(0.50*RIGHT)
        inp[1].shift(0.25*RIGHT)
        inp[3].scale(0.75).shift(0.25*LEFT)
        self.play(Write(title))
        self.wait()
        self.play(Write(intro_text))
        self.wait()
        self.play(ShowCreation(machine.scale(0.75).shift(0.75*DOWN)), run_time=4)
        self.wait()
        F = TexMobject("f(x) =", "x", "^2", "+", "2", "x", "+", "3").move_to(body.get_center()).scale(0.75).shift(0.5*DOWN + 0.25*RIGHT)
        cf = F.copy()
        ff = cf.copy()
        origf = TexMobject("f(x) =", "x", "^2", "+", "2", "x", "+", "3").move_to(body.get_center()).scale(0.75).shift(0.5*DOWN + 0.25*RIGHT)
        f = TexMobject("f(x) =", "x", "^2", "+", "2", "x", "+", "3").move_to(body.get_center()).scale(0.75).shift(0.5*DOWN + 0.25*RIGHT)
        sub1 = TexMobject("f(2) =", "2", "^2", "+", "2\cdot", "2", "+", "3").move_to(body.get_center()).scale(0.75).shift(0.5*DOWN + 0.25*RIGHT)
        sub2 = TexMobject("f(1) =", "1", "^2", "+", "2\cdot", "1", "+", "3").move_to(body.get_center()).scale(0.75).shift(0.5*DOWN + 0.25*RIGHT)
        sub3 = TexMobject("f(\\clubsuit) =", "\\clubsuit", "^2", "+", "2\cdot", "\\clubsuit", "+", "3").move_to(body.get_center()).scale(0.75).shift(0.5*DOWN + 0.25*RIGHT)
        sub4 = TexMobject("f(x^2) =", "(x^2)", "^2", "+", "2\cdot", "(x^2)", "+", "3").move_to(body.get_center()).scale(0.50).shift(0.5*DOWN + 0.25*RIGHT)
        fsub1 = TexMobject("f(2) = 11").move_to(body.get_center()).scale(0.75).shift(0.5*DOWN + 0.25*RIGHT)
        fsub2 = TexMobject("f(1) = 6").move_to(body.get_center()).scale(0.75).shift(0.5*DOWN + 0.25*RIGHT)
        fsub4 = TexMobject("f(x^2) = x^4 + 2x^2 + 3").move_to(body.get_center()).scale(0.75).shift(0.5*DOWN + 0.25*RIGHT)
        op1 = TexMobject("11").move_to(body.get_center()).scale(0.75).shift(2.75*DOWN + 3.1*RIGHT)
        op2= TexMobject("6").move_to(body.get_center()).scale(0.75).shift(2.75*DOWN + 3.1*RIGHT)
        op3 = TexMobject("\\clubsuit", "^2", "+", "2", "\\clubsuit", "+", "3").move_to(body.get_center()).scale(0.35).shift(2.75*DOWN + 3.1*RIGHT)
        op4 = TexMobject("x^4 + 2x^2 + 3").move_to(body.get_center()).scale(0.35).shift(2.75*DOWN + 3.1*RIGHT)
        self.play(FadeIn(f))
        self.wait()
        self.play(FadeInFrom(inp[0], UP))
        self.wait()
        self.play(FadeOutAndShiftDown(inp[0]))
        self.wait()
        self.play(ReplacementTransform(f, sub1))
        self.wait()
        self.play(ReplacementTransform(sub1,fsub1))
        self.wait()
        self.play(FadeInFrom(op1, UP), ReplacementTransform(fsub1, origf))
        self.wait()
        self.play(FadeOutAndShiftDown(op1))
        self.wait()
        self.play(FadeInFrom(inp[1], UP))
        self.wait()
        self.play(FadeOutAndShiftDown(inp[1]))
        self.wait()
        self.play(ReplacementTransform(origf, sub2))
        self.wait()
        self.play(ReplacementTransform(sub2,fsub2))
        self.wait()
        self.play(FadeInFrom(op2, UP), ReplacementTransform(fsub2, F))
        self.wait()
        self.play(FadeOutAndShiftDown(op2))
        self.wait()
        self.play(FadeInFrom(inp[2], UP))
        self.wait()
        self.play(FadeOutAndShiftDown(inp[2]))
        self.wait()
        self.play(ReplacementTransform(F, sub3))
        self.wait()
        self.play(FadeInFrom(op3, UP), ReplacementTransform(sub3, cf))
        self.wait()
        self.play(FadeOutAndShiftDown(op3))
        self.wait()
        self.play(FadeInFrom(inp[3], UP))
        self.wait()
        self.play(FadeOutAndShiftDown(inp[3]))
        self.wait()
        self.play(ReplacementTransform(cf, sub4))
        self.wait()
        self.play(ReplacementTransform(sub4,fsub4))
        self.wait()
        self.play(FadeInFrom(op4, UP), ReplacementTransform(fsub4, ff))
        self.wait()
        self.play(FadeOutAndShiftDown(op4))
        self.wait()
        self.play(Write(exp_text))
        self.wait(4)