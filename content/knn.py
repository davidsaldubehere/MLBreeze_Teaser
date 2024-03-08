from manim import *

class NearestNeighbor(Scene):
    def construct(self):
        blue_points = [(0, 0, 0), (4, 2, 0), (1, 1, 0), (-1, 2, 0), (-2, -1, 0), (-3, 1,0)]
        dots = VGroup()
        for point in blue_points:
            dots.add(Dot(point, color=BLUE))
        self.play(Create(dots))

        red = [(0, 1, 0), (3, 2, 0), (1, 4, 0), (-2, 1, 0), (-3, -1, 0), (-2, 1,0)]
        dots = VGroup()
        for point in red:
            dots.add(Dot(point, color=RED))
        self.play(Create(dots))
        self.wait(1)
        #Add text
        text = Text("Now lets try classfiy a new point", font_size=25).move_to(UL*3)
        self.play(Write(text))
        self.wait(1)
        #Add new point
        new_point = Dot((2, 2, 0), color=GREEN)
        self.play(Create(new_point))
        self.wait(1)
        #Add text
        text1 = Text("Now we calculate distances to each existing point", font_size=25).move_to(UL*3)
        self.play(Transform(text, text1))
        self.wait(1)
        #Add lines
        lines = VGroup()
        for point in blue_points:
            lines.add(Line(new_point.get_center(), point, color=BLUE))
        for point in red:
            lines.add(Line(new_point.get_center(), point, color=RED))
        self.play(Create(lines))
        self.wait(1)
        #Add text
        text2 = Text("Now we find the nearest point", font_size=25).move_to(UL*3)
        self.play(Transform(text, text2))
        self.wait(1)
        self.remove(lines)
        #Add line
        line = Line(new_point.get_center(), red[1], color=RED)
        self.play(Create(line))
        self.wait(1)
        #Add text
        text3 = Text("The nearest point is red", font_size=25).move_to(UL*3)
        self.play(Transform(text, text3))
        self.wait(1)
        text4 = Text("So the new point is classified as red", font_size=25).move_to(UL*3)
        self.play(Transform(text, text4))
        self.remove(line)

        new_point.set_color(RED)
        self.wait(1)
        

class NearestNeighbor3(Scene):
    def construct(self):
        blue_points = [(0, 0, 0), (4, 2, 0), (1, 1, 0), (-1, 2, 0), (-2, -1, 0), (-3, 1, 0)]
        red_points = [(0, 1, 0), (3, 2, 0), (1, 4, 0), (-2, 1, 0), (-3, -1, 0), (-2, 1, 0)]
        new_point_coordinates = (2, 2, 0)
        k = 3  # Number of nearest neighbors

        # Create blue points
        blue_dots = VGroup(*[Dot(point, color=BLUE) for point in blue_points])
        self.play(Create(blue_dots))

        # Create red points
        red_dots = VGroup(*[Dot(point, color=RED) for point in red_points])
        self.play(Create(red_dots))

        # Add text
        text = Text("Now let's try classify a new point using K = 3", font_size=25).move_to(UL * 3)
        self.play(Write(text))
        self.wait(1)

        # Create new point
        new_point = Dot(new_point_coordinates, color=GREEN)
        self.play(Create(new_point))
        self.wait(1)

        # Calculate distances to each existing point
        distances = []
        for point in blue_points + red_points:
            dist = np.linalg.norm(np.array(point) - np.array(new_point_coordinates))
            distances.append((dist, point))

        # Sort distances
        distances.sort(key=lambda x: x[0])

        # Find the nearest k points
        nearest_k_points = [point for dist, point in distances[:k]]

        # Classify based on majority vote
        blue_count = sum(1 for point in nearest_k_points if point in blue_points)
        red_count = sum(1 for point in nearest_k_points if point in red_points)

        if blue_count > red_count:
            classification = BLUE
            classification_text = "So, the new point is classified as blue."
        elif red_count > blue_count:
            classification = RED
            classification_text = "The new point is classified as red."
        else:
            classification = WHITE
            classification_text = "The new point cannot be classified."

        # Add text
        text1 = Text("Of the nearest 3 points, 2 are blue and 1 is red.", font_size=25).move_to(UL * 3)
        self.play(Transform(text, text1))
        self.wait(2)
        text2 = Text(classification_text, font_size=25).move_to(UL * 3)
        self.play(Transform(text, text2))
        self.wait(1)

        # Highlight nearest k points
        k_points_group = VGroup(*[Dot(point, color=YELLOW) for point in nearest_k_points])
        self.play(Create(k_points_group))
        self.wait(1)

        new_point.set_color(classification)
        self.wait(1)