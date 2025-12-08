class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
    
    def surface_area(self):
        return 2 * 3.14159 * self.radius * (self.height + self.radius)    
               
    def volume(self):
        return 3.14159 * (self.radius ** 2) * self.height
        
  
cylinder = Cylinder(5,4)

print(cylinder.surface_area())
print(cylinder.volume())



