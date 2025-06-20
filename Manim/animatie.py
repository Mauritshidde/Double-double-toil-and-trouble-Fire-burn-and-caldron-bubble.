from manim import *

class Stokes(Scene):
    def construct(self):
        formula = MathTex(r"F_e = (\rho_p - \rho_f)g\frac{3}{2} \pi R^3")
        VGroup(formula, formula).arrange(DOWN)
        self.play(
            Write(formula, run_time=3.5),
        )
        # wait during the speaking
        self.wait(3)

        self.play(formula.animate.to_edge(DR))
        # fade out the text
        self.play(
            FadeOut(formula, run_time=2)
        )
        self.wait(1)