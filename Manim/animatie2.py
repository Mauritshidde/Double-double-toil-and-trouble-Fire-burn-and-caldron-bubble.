from manim import *

class StokesSinking(Scene):
    def construct(self):
        #formule staat 10 seconden op midden van scherm
        formula = MathTex(r"F = 6 \pi \eta r v", font_size=60)
        self.play(Write(formula))
        self.wait(10)

        # formule beweegt
        self.play(formula.animate.to_edge(UP))

        # water
        water = FunctionGraph(
            lambda x: 0.2 * np.sin(2 * x),
            x_range=[-7, 7],
            color=BLUE
        ).shift(UP * 2)
        self.play(Create(water))

        # bal
        start_y = 1.7
        ball = Dot(UP * start_y, radius=0.3, color=BLUE)
        self.add(ball)

        #  Krachtvectoren bij bal
        g_vec = Arrow(
            ball.get_center(),
            ball.get_center() + DOWN * 1.2,
            color=RED, buff=0
        ).set_stroke(width=8)
        drag_vec = Arrow(
            ball.get_center(),
            ball.get_center() + UP * 0.05,
            color=GREEN, buff=0
        ).set_stroke(width=8)
        g_label = MathTex("F_g", color=RED).next_to(g_vec, RIGHT)
        drag_label = MathTex("F_{drag}", color=GREEN).next_to(drag_vec, LEFT)

        #beweging vecotren met bal
        def update_g_vec(mob):
            mob.put_start_and_end_on(ball.get_center(), ball.get_center() + DOWN * 1.2)
        def update_drag_vec(mob):
            length = 0.05 + (1.2 - 0.05) * self.drag_alpha
            mob.put_start_and_end_on(ball.get_center(), ball.get_center() + UP * length)

        g_vec.add_updater(update_g_vec)
        drag_vec.add_updater(update_drag_vec)
        g_label.add_updater(lambda mob: mob.next_to(g_vec, RIGHT))
        drag_label.add_updater(lambda mob: mob.next_to(drag_vec, LEFT))
        self.drag_alpha = 0  # Startwaarde voor drag-vector

        self.add(g_vec, drag_vec, g_label, drag_label)

        #Bal staat 8 seconden stil 
        self.wait(8)

        #Bal versnelt
        def set_drag_alpha(a):
            self.drag_alpha = a
        self.play(
            ball.animate.shift(DOWN * 0.8),
            UpdateFromAlphaFunc(drag_vec, lambda m, a: set_drag_alpha(a)),
            run_time=1.2,
            rate_func=rate_functions.ease_in_cubic
        )
        self.drag_alpha = 1  # drag op max

        #constante snelheid
        self.play(
            ball.animate.shift(DOWN * 3.2),
            run_time=2.2,
            rate_func=linear
        )

        self.wait(1)