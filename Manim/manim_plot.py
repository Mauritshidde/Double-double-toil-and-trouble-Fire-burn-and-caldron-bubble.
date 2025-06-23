from manim import *
# , 3.5768e-04, 30, 2, 100
# , 6.7676e-04, 30, 2, 100
# , 7.6706e-04, 30, 3, 100
# , 0.00191279, 30, 4, 100
# , 0.00391777, 30, 5, 100
# , 0.00330728, 30, 6, 100
# 5.47462358, 0.00742593, 30, 2, 125
# 6.78592863, 0.01148318, 30, 3, 125
# 8.28045684, 0.01575730, 30, 4, 125
# 7.95816682, 0.01628910, 30, 5, 125
# 5.80091826, 0.01208115, 30, 6, 125
class lin_plot(Scene):
    def construct(self):
        axes = Axes(
            x_range = [0, 7, 1],
            y_range = [0, 4, 0.25],
            x_length = 10,
            y_length = 10,
            axis_config = {"include_tip": True},
        )
        axes.add_coordinates()
        axes.scale(0.6).to_edge(DOWN)

        self.play(Create(axes))

        points = [(2, 1.20943487), (2, 1.5774861), (3, 1.55615741), (4, 2.40585141), (5, 3.43421192), (6, 1.77329651)]
        points2 = [(2, 1.20943487), (2, 1.5774861), (3, 1.55615741), (4, 2.40585141), (5, 3.43421192), (6, 1.77329651)]

        # Plot the points
        dots = VGroup(*[
            Dot(point=axes.coords_to_point(x, y), color=RED)
            for x, y in points
        ])

        dots = []
        for x, y in points:
            dot = VGroup(*[
                Dot(point=axes.coords_to_point(x, y), color=RED)
            ])
            self.play(FadeIn(dot, shift=UP))
            dots.append(dot)

        self.wait(2)

        for i in dots:
            self.play(FadeOut(i), SHIFT=DOWN)

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

        self.play(Create(axes))
        a = 1.33
        b = 0.62
        def fit(x, a=1.32749239, b=0.61929411):
            return a * x**b
        
        graph = axes.plot(fit, color=PINK)
        self.play(Write(graph))

        label = axes.get_graph_label(graph, label="y = "+str(a)+"x^{"+str(b)+"}", color=RED)
        label.to_edge(LEFT)
        self.play(Write(label))   

        self.wait(2)