from manim import *

class RotatingCubeWithProjection(ThreeDScene):
    def construct(self):
        # Create the 3D cube
        self.cube = Cube(side_length=2)
        self.cube.move_to(ORIGIN)
        self.add(self.cube)

        # Create the plane
        self.plane = NumberPlane(x_range=(-4, 4), y_range=(-4, 4))
        self.plane.rotate(90 * DEGREES, RIGHT)
        self.plane.shift(DOWN * 1)
        self.add(self.plane)

        # Create the dots
        self.dots = VGroup(*[Dot(color=BLUE) for _ in range(8)])
        self.add(self.dots)

        # Rotate the cube and update the dots
        self.begin_3dillusion_camera_rotation(rate=2 * DEGREES)
        self.cube.add_updater(self.update_dots)
        self.wait(4)
        self.cube.remove_updater(self.update_dots)
        self.stop_3dillusion_camera_rotation()
        self.wait(2)

    def update_dots(self, cube, dt):
        # Get the vertices of the cube
        vertices = cube.get_points()

        # Project the vertices onto the plane
        projected_vertices = [self.camera.project_point_onto_screen(v) for v in vertices]

        # Update the positions of the dots
        for i, dot in enumerate(self.dots):
            dot.move_to(projected_vertices[i])