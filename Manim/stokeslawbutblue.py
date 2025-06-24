from manim import *

class StokesLaw(Scene):
    def construct(self):
        formula = MathTex(r"\vec{F_d} = - 6 \pi \eta r \vec{v}",
                           color = BLUE_A)
        formula.scale(1.5)
        self.play(Write(formula))
        self.wait(2)

