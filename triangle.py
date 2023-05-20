from figure import Figure

class Triangle(Figure):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Assuming equilateral triangle for simplicity
        return 3 * self.base