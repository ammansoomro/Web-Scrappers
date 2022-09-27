# Class Rectangle 

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    # Function to increase size
    def increase_size(self, lentgh, width):
        self.length += lentgh
        self.width += width

    def __str__(self):
        return f"Rectangle: length = {self.length}, width = {self.width}"

# Class Cuboid inherits from class Rectangle

class Cuboid(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height
    
    def increase_size(self, lentgh, width, height):
        super().increase_size(lentgh, width)
        self.height += height

    def __str__(self):
        return f"Cuboid: length = {self.length}, width = {self.width}, height = {self.height}"

if __name__ == "__main__":
    print("==================== Rectangle ====================")
    # Create object Rectangle
    rectangle = Rectangle(1, 2)
    # Print dimensions
    print(rectangle)
    # Print area
    print(f"Area = {rectangle.area()}")
    # increase dimensions
    rectangle.length += 1
    rectangle.width += 1
    # Print dimensions
    print(rectangle)
    # print area
    print(f"Area = {rectangle.area()}")

    print("==================== Cuboid ====================")
    # Create object Cuboid
    cuboid = Cuboid(1, 2, 3)
    # Print dimensions
    print(cuboid)
    # Print area
    print(f"Area = {cuboid.volume()}")
    # increase dimensions
    cuboid.length += 1
    cuboid.width += 1
    cuboid.height += 1
    # Print dimensions
    print(cuboid)
    # print area
    print(f"Area = {cuboid.volume()}")