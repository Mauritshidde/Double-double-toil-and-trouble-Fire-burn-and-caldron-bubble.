from manim import *
import math as m
import json

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

        x_label = MathTex(r"\text{Time in seconds}").next_to(axes.x_axis, DOWN, buff=0.2).scale(0.6)
        y_label = MathTex(r"\text{Distance travelled in cm}").rotate(PI/2).next_to(axes.y_axis, LEFT, buff=0.2).scale(0.6)

        with open('../Code/data/pillen.json', 'r') as openfile:
            data = json.load(openfile)

        vals = []
        pill_size = []
        for i in data:
            vals.append(i.get('fit2'))
            pill_size.append(i.get('object_length'))
        
        vals_1 = []
        pill_size_1 = []
        vals_2 = []
        pill_size_2 = []
        for i in range(6):
            vals_1.append(vals[i])
            pill_size_1.append(pill_size[i] + 2*m.sqrt(10/m.pi))

        for i in range(6):
            vals_2.append(vals[i+6])
            pill_size_2.append(pill_size[i+6] + 2*m.sqrt(10/m.pi))

        self.play(Create(axes), Write(x_label), Write(y_label))

        points = [(2, 1.20943487), (2, 1.5774861), (3, 1.55615741), (4, 2.40585141), (5, 3.43421192), (6, 1.77329651)]
        points_2 = [()]

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

