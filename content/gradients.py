from manim import *

class SimplePlot(Scene):
    def construct(self):
        my_plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-10, 10, 1], x_length=10, y_length=10, 
            background_line_style={"stroke_opacity": 0.5, "stroke_color": BLUE_D},
            ).add_coordinates()

        my_function = my_plane.plot(lambda x: x**2, color=GREEN, x_range=[-5, 5])

        label = MathTex("f(x) = x^2").to_corner(UL)

        self.play(Create(my_plane), Write(label), Create(my_function), run_time=4)

