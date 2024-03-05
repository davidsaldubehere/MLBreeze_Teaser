from manim import *

class GradientDescentScene(ThreeDScene):
    def construct(self):
        # Define the function to optimize (example: f(x, y) = x^2 + y^2)
        def function(x, y):
            return x**2 + y**2
        
        # Define the partial derivatives of the function
        def df_dx(x, y):
            return 2 * x
        
        def df_dy(x, y):
            return 2 * y
        
        # Initialize starting point for gradient descent
        point = VectorizedPoint([3, 3, function(3, 3)])
        self.add(point)
        
        # Add labels for axes
        x_label = Text("x", font_size=24).next_to(point, RIGHT)
        y_label = Text("y", font_size=24).next_to(point, UP)
        z_label = Text("z", font_size=24).next_to(point, OUT)
        self.add(x_label, y_label, z_label)
        
        # Add text to explain gradient descent
        text = Text("Gradient Descent", font_size=36).to_edge(UP)
        self.add(text)
        
        # Define the update function for gradient descent
        def update_point(point, dt):
            x, y, _ = point.get_location()
            grad_x = df_dx(x, y)
            grad_y = df_dy(x, y)
            step_size = 0.1
            
            new_x = x - step_size * grad_x
            new_y = y - step_size * grad_y
            new_z = function(new_x, new_y)
            point.move_to([new_x, new_y, new_z])
        
        # Animate gradient descent
        self.play(Write(text))
        self.wait(0.5)
        self.play(UpdateFromFunc(point, update_point), run_time=3)
        self.wait()
