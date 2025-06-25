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

