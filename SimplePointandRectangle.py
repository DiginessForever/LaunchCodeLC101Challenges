class Point:
    x = 0
    y = 0

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
    def __eq__(self, otherPoint):
        if self.x == otherPoint.get_x() and self.y == otherPoint.get_y():
            return True
        else:
            return False
    
class Rectangle:
    lowerLeft  = Point(0,0)
    upperLeft  = Point(0,1)
    upperRight = Point(1,1)
    lowerRight = Point(1,0)
    height = 0
    width = 0
    
    def __init__(self, lowerLeftPoint, height, width):
        self.lowerLeft = lowerLeftPoint
        self.height = height
        self.width = width
        self.upperLeft = Point(self.lowerLeft.get_x(), self.lowerLeft.get_y() + height)
        self.upperRight = Point(self.lowerLeft.get_x() + width, self.lowerLeft.get_y() + height)
        self.lowerRight = Point(self.lowerLeft.get_x() + width, self.lowerLeft.get_y())
        
    def __repr__(self):
        return "I am a rectangle with lower left point at: " + str(lowerLeft) + " , width: " + self.width + ", height: " + self.height
    
    def getArea(self):
        return self.height * self.width
    
    def getAreaFromPoints(self):
        width = self.lowerLeft.get_x() - self.lowerRight.get_x()
        if (width < 0):
            width *= -1
        height = self.lowerLeft.get_y() - self.upperLeft.get_y()
        if (height < 0):
            height *= -1
        if (width * height == 0):
            print("Width: " + str(width) + ", height: " + str(height))
        return width * height
    
    def checkMyAssumptions(self):
        if (self.getArea() == self.getAreaFromPoints()):
            return "width * heigth == point width * point height calculations"
        else:
            string1 = "Something differs between assumed width and height versus point positions"
            #string2 = "Width * Height = " + str(width * height) + ", and pointwid
            return string1
        
    def __eq__(self, otherRect):
        isTrue = True
        if (self.lowerLeft != otherRect.lowerLeft):
            isTrue = False
        if (self.lowerRight != otherRect.lowerRight):
            isTrue = False
        if (self.upperLeft != otherRect.upperLeft):
            isTrue = False
        if (self.upperRight != otherRect.upperRight):
            isTrue = False
        return isTrue
    
myPoint = Point(1,1)
print(myPoint)
print(myPoint.distance_from_origin())

myRect = Rectangle(Point(0,0), 1, 1)

print("My rectangle's area: " + str(myRect.getArea()))
print("My rectangle's assumed area from my method getPointFromArea(): " + str(myRect.getAreaFromPoints()))
print(myRect.checkMyAssumptions())
print("Lower left point: " + str(myRect.lowerLeft))
print("Upper left point: " + str(myRect.upperLeft))
print("Upper right point: " + str(myRect.upperRight))
print("Lower left point: " + str(myRect.lowerRight))
