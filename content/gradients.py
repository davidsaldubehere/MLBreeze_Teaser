from manim import *

class First(Scene):
    def construct(self):
        my_plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-10, 10, 1], x_length=10, y_length=10, 
            background_line_style={"stroke_opacity": 0.5, "stroke_color": BLUE_D},
            ).add_coordinates()

        my_function = my_plane.plot(lambda x: x**2, color=GREEN, x_range=[-5, 5])

        label = MathTex("f(x) = x^2").to_corner(UL)

        self.play(Create(my_plane), Write(label), Create(my_function), run_time=4)

class Second(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            z_length=10,
            x_axis_config={"include_numbers": True, "include_ticks": True},
            y_axis_config={"include_numbers": True, "include_ticks": True},
            z_axis_config={"include_numbers": True, "include_ticks": True},
        )
        
        graph = Surface(
            lambda u, v: np.array([
                u,
                v,
                u**2 + v**2
            ]),
            u_range=[-5, 5],
            v_range=[-5, 5],
            checkerboard_colors=[BLUE_D, BLUE_D],
        )
        
        self.add(axes)
        self.play(Create(graph))
        self.wait(2)
        self.begin_ambient_camera_rotation(
            rate = PI/10, about="theta"
        )
        self.wait(10)
        self.stop_ambient_camera_rotation()

class Third(Scene):
    def construct(self):
        my_plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-10, 10, 1], x_length=10, y_length=10, 
            background_line_style={"stroke_opacity": 0.5, "stroke_color": BLUE_D},
            ).add_coordinates()

        def func(x):
            return x**2

        def deriv(x):
            return 2*x

        my_function = my_plane.plot(func, color=GREEN, x_range=[-5, 5])
        label = MathTex("f(x) = x^2").to_corner(UL)
        self.play(Create(my_plane), Write(label), Create(my_function), run_time=1)
        # Add tangent lines and points
        tangent_points = [.5, 1.5, 2.5]  # Points where tangent lines will be drawn
        for x_coord in tangent_points:
            y_coord = func(x_coord)
            slope = deriv(x_coord)
            tangent_line = Line(
                my_plane.coords_to_point(x_coord, y_coord),
                my_plane.coords_to_point(x_coord + 1, y_coord + slope),
                color=RED
            )
            tangent_point = Dot(my_plane.coords_to_point(x_coord, y_coord), color=YELLOW)
            point_label = Tex(f"$f'(x) = {deriv(x_coord)}$").next_to(tangent_point,  RIGHT + RIGHT)

            self.play(Create(tangent_line), Create(tangent_point), Write(point_label))





class Fourth(Scene):
    
    def construct(self):
        # Display the function
        function_text = MathTex("f(x, y) = x^2 + y^2").to_corner(UL)
        self.play(Write(function_text))

        text=MathTex(
            "\\frac{\\partial f}{\\partial}(x, y) = ","\\frac{\\partial f}{\\partial x} x^2 + c",",  ","\\frac{\\partial f}{\\partial y} c + y^2"
        )
        #Now the result of the gradient is displayed

        result = MathTex(
            "\\nabla f(x, y) = \\begin{bmatrix} 2x \\\\ 2y \\end{bmatrix}"
        ).next_to(text, DOWN)
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)

        # Add text above the framebox
        text_above_framebox = Text("Treat y as constant").move_to([0, 2, 0])
        text_above_framebox.set_color(RED)
        text_above_framebox2 = Text("Treat x as constant").move_to([0, 2, 0])
        text_above_framebox2.set_color(BLUE)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
            Write(text_above_framebox),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
            ReplacementTransform(text_above_framebox,text_above_framebox2),
        )
        self.wait()
        self.play(Write(result))
        # Animation for partial derivative with respect to x


class Fifth(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            z_length=10,
            x_axis_config={"include_numbers": True, "include_ticks": True},
            y_axis_config={"include_numbers": True, "include_ticks": True},
            z_axis_config={"include_numbers": True, "include_ticks": True},
        )
        self.play(Create(axes))
        # Define the function
        def f(x, y):
            return x**2 + y**2
        
        # Define the gradient of the function
        def gradient(x, y):
            return np.array([2 * x, 2 * y, 0])  # Gradient of f(x, y) = x^2 + y^2
        
        # Create surface
        graph = Surface(
            lambda u, v: np.array([
                u,
                v,
                u**2 + v**2
            ]),
            u_range=[-5, 5],
            v_range=[-5, 5],
            checkerboard_colors=[BLUE_D, BLUE_D],
        )
        self.play(Create(graph))
        
        # Plot gradient vectors
        points = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1,1)]  # List of points
        
        for point in points:
            x, y = point
            z = f(x, y)
            
            # Add a dot at the point
            dot = Dot(np.array([x, y, z]), color=RED)
            self.add(dot)
            
            # Add gradient vector
            gradient_vector = Arrow3D(start=np.array([x, y, z]), end=np.array([x, y, z]) + gradient(x, y), color=RED)
            self.add(gradient_vector)
                
        self.begin_ambient_camera_rotation(
            rate=PI/10, about="theta"
        )
        self.wait(10)
        self.stop_ambient_camera_rotation()



class Sixth(Scene):
    def construct(self):

        k = ValueTracker(-3)  # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-8, 9, 2], y_length=5)
            .add_coordinates()
            .shift(LEFT * 3.5)
        )

        func1 = plane1.plot(
            lambda x: x**2, x_range=[-3, 3], color=RED_C
        )
        func1_lab = (
            MathTex("f(x)=x^2")
            .set(width=2.5)
            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope = always_redraw(
            lambda: plane1.get_secant_slope_group(
                x=k.get_value(),
                graph=func1,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
        )

        dot = always_redraw(
            lambda: Dot().move_to(
                plane1.c2p(k.get_value(), func1.underlying_function(k.get_value()))
            )
        )

        # Adding Mobjects for the second plane
        plane2 = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-10, 6, 2], y_length=5)
            .add_coordinates()
            .shift(RIGHT * 3.5)
        )

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: 2 * x, x_range=[-3, k.get_value()], color=GREEN
            )
        )
        func2_lab = (
            MathTex("f'(x)=2x")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )


        # Adding the slope value stuff
        slope_value_text = (
            Tex("Slope value: ")
            .next_to(plane1, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2.underlying_function(k.get_value()))
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()

        function_value_text = (
            Tex("Function value: ")
            .next_to(plane2, DOWN, buff=0.1)
            .set_color(RED_C)
            .add_background_rectangle()
        )

        function_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2.underlying_function(k.get_value()))
            .next_to(function_value_text, RIGHT, buff=0.1)
            .set_color(RED_C)
        ).add_background_rectangle()

        # Playing the animation
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane1),
                DrawBorderThenFill(plane2),
                Create(func1),
                Write(func1_lab),
                Write(func2_lab),
                run_time=5,
                lag_ratio=0.5,
            )
        )
        self.add(moving_slope, func2, slope_value, slope_value_text, function_value, function_value_text, dot)
        self.play(k.animate.set_value(3), run_time=15, rate_func=linear)
        self.wait()
