class Line:
    def __init__(self, x_points, y_points):
        self.x_points = x_points
        self.y_points = y_points
        
    
    def slope(self): 
        x1,x2 = self.x_points
        y1,y2 = self.y_points       
               
        if x2 - x1 == 0:
            return 'Slope is undefined for vertical lines'
        
        return (y2 - y1) / (x2 - x1)

    def distance(self):
        x1,x2 = self.x_points
        y1,y2 = self.y_points
        return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

x_points = (0,0)
y_points = (0,0)

line = Line(x_points, y_points)

print(line.slope())
print(float(line.distance()))



