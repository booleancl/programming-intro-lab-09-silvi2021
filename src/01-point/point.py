import math

class Point:
    def __init__(self,x = 0,y = 0):
        self.move(x,y)
        
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)
        
    def distance_to(self,other_point):
        distance_x = self.x - other_point.x
        distance_y = self.y - other_point.y

        distance = math.sqrt(distance_x**2 + distance_y**2)
        
        return distance

    

    
        


    
