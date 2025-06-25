from manim import *

class wortel_fit(Scene):
    def construct(self):
        axes = Axes(
            x_range = [0, 170, 10],
            y_range = [0, 35, 5],
            x_length = 15,
            y_length = 10,
            axis_config = {"include_tip": True},
        )

        axes.add_coordinates()
        axes.scale(0.3).to_edge(LEFT)

        x_label = MathTex(r"\text{Time in seconds}").next_to(axes.x_axis, DOWN, buff=0.2).scale(0.4)
        y_label = MathTex(r"\text{Distance travelled in cm}").rotate(PI/2).next_to(axes.y_axis, LEFT, buff=0.2).scale(0.4)

        self.play(Create(axes), Write(x_label), Write(y_label))
        
        a = 0.9487431604208888
        a = round(a, 3)
        b = 0.5239175627816949
        b = round(b, 3)
        def fit(x, a=1.32749239, b=0.61929411):
            return a * x**b
        
        graph = axes.plot(fit, color=PINK)
        label = axes.get_graph_label(graph, label="d = "+str(a)+"t^{"+str(b)+"}", color=RED)
        label.next_to(axes, DOWN).shift(0.5 * DOWN)
        
        self.play(Write(graph), Write(label), run_time=6)
        # self.play(Write(label), run_time=1)   

        self.wait(2)