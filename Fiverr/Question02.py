# Class Cuboid

class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def volume(self):
        return self.length * self.width * self.height

    def __str__(self):
        return f"Cuboid: length = {self.length}, width = {self.width}, height = {self.height}